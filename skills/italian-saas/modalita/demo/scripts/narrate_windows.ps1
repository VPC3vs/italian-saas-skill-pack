[CmdletBinding(DefaultParameterSetName = 'Speak')]
param(
    [Parameter(Mandatory = $true, ParameterSetName = 'Speak')]
    [string]$TextPath,
    [Parameter(Mandatory = $true, ParameterSetName = 'Speak')]
    [string]$OutputWav,
    [Parameter(ParameterSetName = 'Speak')]
    [string]$VoiceName,
    [Parameter(ParameterSetName = 'Speak')]
    [ValidateRange(-4, 4)]
    [int]$Rate = 0,
    [Parameter(Mandatory = $true, ParameterSetName = 'List')]
    [switch]$ListVoices
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech
$demoSynth = New-Object System.Speech.Synthesis.SpeechSynthesizer
try {
    $demoVoices = @($demoSynth.GetInstalledVoices() | Where-Object {
        $_.Enabled -and $_.VoiceInfo.Culture.Name -eq 'it-IT' -and
        $_.VoiceInfo.Gender -eq [System.Speech.Synthesis.VoiceGender]::Female
    })
    if ($ListVoices) {
        $demoVoices | ForEach-Object {
            $_.VoiceInfo | Select-Object Name, Culture, Gender
        }
        return
    }
    $demoVoice = $demoVoices | Where-Object {
        -not $VoiceName -or $_.VoiceInfo.Name -eq $VoiceName
    } | Select-Object -First 1
    if (-not $demoVoice) {
        throw 'No enabled Italian female voice matches. Run with -ListVoices or use another available speech provider.'
    }
    $demoText = Get-Content -LiteralPath $TextPath -Raw -Encoding UTF8
    if ([string]::IsNullOrWhiteSpace($demoText)) {
        throw 'The narration text is empty.'
    }
    $demoOutput = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($OutputWav)
    if ([IO.Path]::GetExtension($demoOutput) -ne '.wav') {
        throw 'OutputWav must end in .wav.'
    }
    if (Test-Path -LiteralPath $demoOutput) {
        throw "Output already exists: $demoOutput"
    }
    [IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($demoOutput)) | Out-Null
    $demoFormat = New-Object System.Speech.AudioFormat.SpeechAudioFormatInfo(
        48000,
        [System.Speech.AudioFormat.AudioBitsPerSample]::Sixteen,
        [System.Speech.AudioFormat.AudioChannel]::Mono
    )
    $demoSynth.SelectVoice($demoVoice.VoiceInfo.Name)
    $demoSynth.Rate = $Rate
    $demoSynth.SetOutputToWaveFile($demoOutput, $demoFormat)
    $demoSynth.Speak($demoText.Trim())
    $demoSynth.SetOutputToNull()
    [pscustomobject]@{
        voice = $demoVoice.VoiceInfo.Name
        culture = $demoVoice.VoiceInfo.Culture.Name
        gender = $demoVoice.VoiceInfo.Gender.ToString()
        engine = 'System.Speech'
        rate = $Rate
        output = $demoOutput
    } | ConvertTo-Json
}
finally {
    $demoSynth.Dispose()
}
