# Produzione con GPT/Codex e Hyperframes

## Capacità e percorsi

Questa è una skill di istruzioni, non un renderer né un servizio GPT. Richiede un agente con accesso ai file e agli strumenti necessari; una chat priva di esecuzione può preparare piano e copy, ma non dichiarare di aver generato un MP4.

Usa i tool realmente disponibili. Risolvi eventuali risorse rispetto alla cartella di questa skill; non usare percorsi Claude, marketplace Claude o nomi di strumenti presunti. Gli esempi shell vanno adattati a PowerShell o alla shell corrente.

Il renderer upstream è Hyperframes: [sito ufficiale](https://hyperframes.heygen.com/). Verifica Node.js, FFmpeg e Hyperframes con la documentazione attuale e l'help della CLI. Usa una versione nota per tutta la produzione, rispettando quella già fissata nel progetto. Non aggiornare dipendenze del prodotto per creare un teaser.

Se disponibili, leggi le skill di dominio `hyperframes-core`, `hyperframes-animation`, `hyperframes-creative`, `hyperframes-keyframes` e `hyperframes-cli`; non sono incluse nel pack e non sono prerequisiti per scrivere il piano. In loro assenza consulta la documentazione ufficiale della versione disponibile. Non presumere che siano agenti o tool callable e non delegare automaticamente. Il brief già definito evita una seconda intervista generica.

I comandi upstream comprendono `npx hyperframes doctor`, `npx hyperframes check` e `npx hyperframes render`; verifica opzioni e directory di esecuzione con l'help prima di usarli. Installa soltanto i componenti necessari nel perimetro autorizzato. Se il renderer è indisponibile, completa piano, storyboard e copy e indica il blocco preciso senza chiamare “video” quei soli materiali.

## Audio e voce

Il pack non include audio di terzi. Usa musica ed effetti forniti o disponibili con diritti appropriati e registra fonte/licenza nel brief. Se mancano, procedi senza quel livello audio e dichiaralo. Rispetta `--no-music` e `--no-sfx` indipendentemente dalla voce.

Con voce disattivata non generare copione parlato, TTS o traccia vocale. Con `--voice` o richiesta equivalente, prepara un copione conciso che completi le immagini, poi usa un provider TTS disponibile che supporti davvero la lingua scelta. Preferisci una voce femminile professionale italiana quando l'utente non specifica altro; usa una voce inglese adatta per EN. Kokoro tramite Hyperframes è utilizzabile se la versione installata espone una voce adatta: verifica l'elenco, non fissare una voce inglese per il testo italiano. Non presumere credenziali, abbonamenti o accesso a un provider OpenAI.

Genera e ascolta un campione con nome del prodotto e parole difficili. Se la voce richiesta non è disponibile, segnala il blocco della narrazione e continua i materiali indipendenti; non consegnare silenziosamente un video muto come se fosse narrato. Misura l'audio finale, adatta le scene e riduci il testo se necessario; non accelerare artificialmente la lettura per rientrare nel target. Mantieni musica ed effetti sotto la voce e controlla clipping, tagli, pause e pronuncia.

Copia solo gli asset scelti dentro `composition/assets/`, con riferimenti relativi nel progetto di rendering. Beat sync e reattività audio sono opzionali: usa i dati realmente estratti e ignora i beat che compromettono lettura o racconto. Non inventare BPM o timestamp. Allinea gli effetti ai gesti visibili e assegna tracce distinte all'audio sovrapposto secondo il contratto Hyperframes attuale.

## Verifica dell'export

Il controllo tecnico della composizione non sostituisce la revisione del render. Ispeziona fotogrammi stabili e transizioni, riproduci il video e ascolta tutto l'audio quando gli strumenti lo consentono. Verifica durata, dimensioni e decodifica con gli strumenti multimediali disponibili. Se non puoi vedere o ascoltare qualcosa, esplicita il limite e non dichiarare quella verifica superata.
