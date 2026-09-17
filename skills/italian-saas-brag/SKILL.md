---
name: italian-saas-brag
description: Trasforma il sito del progetto corrente in un breve video di lancio curato e condivisibile con Hyperframes. Usa per /brag, facciamolo conoscere, crea un video di lancio o condividi ciò che ho costruito. Legge direttamente il codice, senza richiedere URL live o screenshot. Italian-first; English and bilingual IT/EN supported.
---

# /brag

L'hai costruito. Ora fallo conoscere.

## Lingua e compatibilità GPT/Codex

Questa è la traduzione italiana della skill Brag originale: stesso workflow, stessi riferimenti tecnici completi, script e asset audio originali. Il testo inglese integrale è in [SKILL.en.md](SKILL.en.md); i riferimenti tecnici restano disponibili in inglese senza tagli.

Usa italiano come lingua predefinita per conversazione, piano, brief, testi a schermo, copione e copy social. Con `--lang en` o richiesta equivalente usa inglese; con `--lang both` produci le versioni italiana e inglese dello stesso video, prima IT e poi EN, in sottocartelle `it/` ed `en/`. Adatta i tempi alla lettura e alla narrazione della lingua scelta; conserva marchi, nomi, identificatori e testo della UI reale.

In Codex puoi invocare `$italian-saas-brag` oppure scrivere `/brag` nella richiesta. Nei riferimenti originali, risolvi `~/.claude/skills/brag/` e `skills/brag/` alla cartella effettiva di questa skill: `$CODEX_HOME/skills/italian-saas-brag/` (normalmente `~/.codex/skills/italian-saas-brag/`) oppure `skills/italian-saas-brag/` nel pack. Sostituisci questi percorsi anche negli esempi `uv`, senza modificare gli script. Adatta solo la sintassi shell al sistema operativo.

La voce rimane Kokoro tramite Hyperframes. L'esempio originale `af_heart` è per l'inglese; per l'italiano usa `npx hyperframes tts --list` e seleziona una voce italiana disponibile nello stesso provider. Non aggiungere selezione tra provider. Se non esiste una voce per la lingua richiesta, segnala quel limite anziché pronunciare l'italiano con una voce inglese o disattivare la narrazione richiesta.

## Interpretazione dell'invocazione (prima di tutto)

Prima di esaminare il progetto, analizza l'intera invocazione `/brag`. Se contiene `--voice`, imposta `voice.enabled = true`. Abilita la narrazione soltanto per quella esecuzione. Non abilitarla automaticamente e non ripiegare sul normale workflow senza voce.

`/brag` trasforma il sito o l'app del progetto corrente in un breve video di lancio curato e condivisibile usando Hyperframes. Ha uno scopo preciso, scelte creative nette e uno spirito divertente.

## Cosa fa questa skill

1. Legge il codice del progetto corrente per capire l'app.
2. Progetta un breve concept Brag specifico per questo progetto.
3. Scrive testi e storyboard del video.
4. Passa a Hyperframes un brief di composizione mirato.
5. Verifica, renderizza e scrive il testo per la condivisione.

## Interpretazione delle opzioni

L'utente può usare linguaggio naturale o opzioni:

```text
/brag
/brag --tone chaotic
/brag --tone polished --format vertical
/brag questo progetto. Fallo sembrare il lancio di una startup assurda.
```

Interpreta queste opzioni:

| Opzione | Valori | Predefinito |
| --- | --- | --- |
| `--tone` | Preset o descrizione libera | Ricavato dal progetto |
| `--format` | `landscape`, `vertical`, `square` | `landscape` |
| `--duration` | Secondi | Automatico (15–25s) |
| `--no-music` | Flag | Musica attiva |
| `--no-sfx` | Flag | Effetti attivi |
| `--title` | Stringa | Ricavato dal progetto |
| `--voice` | Flag | Narrazione disattivata |
| `--lang` | `it`, `en`, `both` | `it` |

La voce è facoltativa. Con `--voice`, usa Kokoro tramite Hyperframes e non aggiungere logica di selezione del provider. Il workflow vocale originale usa intenzionalmente un solo provider.

Il tono può essere un preset (`default`, `polished`, `yc-parody`, `chaotic`, `deadpan`, `cinematic`, `app-store`) oppure una direzione creativa come “finto lancio Series A del 2016”, “mostra museale” o “pubblicità di un gioco mobile esageratamente prodotta”.

Con una direzione libera, scegli il preset più vicino per ritmo e struttura, ma conserva la direzione dell'utente nel piano e nel brief di composizione.

## Indicazioni per la narrazione

Con `--voice`, scrivi una narrazione che completi le immagini, senza limitarsi a leggere il testo visibile, segua il ritmo delle scene, suoni naturale e colloquiale e colleghi fluidamente le scene. Mantieni il copione conciso e specifico del prodotto, così la voce diventa parte del montaggio e non una traccia separata sovrapposta.

---

## Cartella di output

Per impostazione predefinita usa `brag-output/`. Per evitare di sovrascrivere esecuzioni precedenti, usa una cartella con timestamp:

```text
brag-output-2026-05-04-143022/
```

Usa un timestamp quando:
- L'utente chiede esplicitamente una nuova esecuzione senza sovrascrivere i risultati precedenti.
- Nel progetto esiste già una cartella `brag-output/`.

Genera il timestamp all'inizio (`YYYY-MM-DD-HHmmss`) e usalo coerentemente per tutti i percorsi dell'esecuzione: piano, brief, composizione, render e copy social. Con `--lang both`, applica la stessa struttura separatamente dentro `it/` ed `en/`.

---

## Passaggio 1: esamina il progetto

**Leggi:** [references/step-1-inspect.md](references/step-1-inspect.md)

Esamina la cartella del progetto ed estrai le informazioni necessarie a pianificare il video Brag.

**Criterio di completamento:** sai rispondere a tutte le 9 domande della griglia di pianificazione Brag.

---

## Passaggio 2: piano e storyboard

**Leggi:** [references/step-2-plan.md](references/step-2-plan.md)

Scrivi `<output-dir>/brag-plan.md`, dove `<output-dir>` è `brag-output/` o la variante con timestamp scelta sopra. Rispondi alla griglia di pianificazione. Scegli un angolo creativo preciso. Scrivi lo storyboard momento per momento, includendo scene, testi, tempi, transizioni e indicazioni SFX.

Quando scegli la musica, includi una breve sezione `Music cue guidance`: leggi il preset della traccia inclusa da `assets/music/cues/`, se presente; altrimenti annota che i cue verranno rilevati durante la composizione. Ora qualsiasi traccia supporta la sincronizzazione ai beat: vedi `references/audio.md`. I metadati dei cue sono soltanto indicazioni temporali facoltative: storia, leggibilità, ritmo e chiarezza del prodotto restano prioritari.

**Criterio di completamento:** `<output-dir>/brag-plan.md` esiste con uno storyboard completo. La somma delle durate delle scene è di 15–25 secondi.

---

## Passaggio 3: passa il lavoro a Hyperframes

**Leggi:** le skill di dominio Hyperframes: `hyperframes-core`, `hyperframes-animation`, `hyperframes-creative`, `hyperframes-keyframes`, `hyperframes-cli`. /brag ha un proprio workflow: non avviare l'intervista iniziale dell'entry point `hyperframes` e non instradare il lavoro verso il suo workflow generico per video promozionali o di lancio.

**Leggi:** [references/step-3-compose.md](references/step-3-compose.md)

**Leggi:** [references/audio.md](references/audio.md)

Scrivi il brief di composizione e usa Hyperframes per creare l'implementazione del video in `<output-dir>/composition/`.

`/brag` decide angolo del prodotto, materiali sorgente, storyboard, tono, formato, selezione audio, indicazioni sui cue musicali e aspettative di consegna. Hyperframes decide struttura concreta della composizione, tempi esatti delle animazioni, meccaniche di animazione, runtime, regole di lint e workflow di rendering.

**Criterio di completamento:** `npx hyperframes check` passa senza errori dentro `<output-dir>/composition/`, l'unico controllo nel browser prima del render; consulta hyperframes-cli per i controlli eseguiti.

---

## Passaggio 4: verifica, renderizza e consegna

**Leggi:** [references/step-4-deliver.md](references/step-4-deliver.md)

Verifica, mostra l'anteprima e renderizza in `<output-dir>/brag.mp4`. Seleziona il fotogramma migliore per il poster `<output-dir>/brag.jpg`, inseriscilo come frame 0 del video per la miniatura iniziale secondo il workflow originale, e scrivi `<output-dir>/share-copy.txt`.

**Criterio di completamento:** `<output-dir>/brag.mp4` esiste. Il poster `<output-dir>/brag.jpg` è scelto dal fotogramma migliore, non da uno arbitrario, ed è incorporato come frame 0 di `brag.mp4`. Il copy social è scritto.

---

## Sistema dei toni

`/brag` include sette preset. Ognuno modifica energia dei testi, ritmo, personalità tipografica e stile delle transizioni. I preset sono punti di partenza, non limiti.

Definizioni complete: [references/tones.md](references/tones.md)

| Tono | Energia | In una frase |
| --- | --- | --- |
| `default` | Giocoso, pulito, pronto da condividere | Il predefinito di buon umore |
| `polished` | Serio, elegante | Per progetti che non sono uno scherzo |
| `yc-parody` | Serietà impassibile da startup | Finta serietà applicata a progetti assurdi |
| `chaotic` | Rapido, rumoroso, aggressivo | Esagerato e fuori controllo |
| `deadpan` | Calmo, asciutto, sottotono | La battuta è che niente è una battuta |
| `cinematic` | Drammatico, da trailer | Grandi movimenti, affermazioni ancora più grandi |
| `app-store` | Fluido, schede funzionalità pulite | Aziendale, ma non noioso |

Consenti sempre a una direzione creativa libera di affinare o sostituire il preset.

---

## Leggi creative

Valgono per ogni video Brag, indipendentemente dal tono.

**Breve.** 15–25 secondi. Non un secondo in più senza un motivo.

**Leggibile.** Mantieni alto il ritmo con movimento e tagli, mai facendo lampeggiare i testi. Ogni riga deve rimanere abbastanza a lungo da essere letta: un'etichetta breve circa 0,8s da ferma; una frase circa 0,3s per parola. Entrata rapida, poi pausa; mai entrata rapida e subito via.

**Specifico.** Il video deve sembrare realizzato per questo preciso progetto, non per un progetto qualsiasi.

**Mostra il prodotto.** Almeno una scena deve mostrare UI, testi o un elemento visivo chiave reali del prodotto. Niente riempitivi astratti.

**Niente linguaggio SaaS generico.** “Ottimizza il tuo workflow” è vietato. Usa i testi e le affermazioni effettivi del progetto.

**L'apertura è tutto.** I primi 2 secondi decidono se qualcuno continua a guardare. Pianifica l'aggancio prima di tutto il resto.

**L'umorismo deve meritarsi il suo posto.** Deve nascere dall'assurdità del progetto, non dallo sforzo di essere divertenti.

**Schema:**

```text
Aggancio (2–3s) → Presentazione (2–4s) → 2–3 punti forti (5–12s) → Battuta finale/chiusura (2–4s)
```

Adattalo. Non tutti i progetti hanno bisogno di esattamente 3 punti forti. Lo schema è una forma iniziale, non un modello rigido.

## Provenienza

Traduzione di [latent-spaces/brag](https://github.com/latent-spaces/brag), commit `1f8d9ade17d0ad4419cca9305fbc1398a4dd5b39`. [Licenza originale](LICENSE). Musica, SFX, cue, analisi e script sono inclusi senza modifiche; i crediti e le note upstream restano negli asset e in [references/audio.md](references/audio.md).
