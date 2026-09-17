---
name: italian-saas-brag
description: Crea brevi video di lancio SaaS con Hyperframes, storyboard, poster e testi social, in italiano predefinito o inglese. Use for launch teasers, /brag, hype reels and bilingual IT/EN product launch videos; per walkthrough formativi estesi usa una skill demo.
---

# Brag — il tuo prodotto, in primo piano

Adattamento di Brag per agenti GPT/Codex con strumenti per file, terminale e rendering. Crea un teaser specifico del prodotto: apertura forte, UI riconoscibile, pochi benefici verificati e chiusura memorabile. Durata predefinita 15–25 secondi; rispetta una durata esplicita diversa.

## Invocazione e lingue

Accetta `$italian-saas-brag`, `/brag` come testo della richiesta, oppure linguaggio naturale. Le opzioni sono convenzioni da interpretare, non comandi CLI registrati.

| Opzione | Valori e comportamento |
| --- | --- |
| `--lang` | `it` predefinito; `en` inglese; `both` due versioni IT/EN separate |
| `--tone` | `default`, `polished`, `yc-parody`, `chaotic`, `deadpan`, `cinematic`, `app-store`, oppure direzione libera |
| `--format` | `landscape` 1920×1080 predefinito; `vertical` 1080×1920; `square` 1080×1080 |
| `--duration` | Secondi richiesti; altrimenti 15–25 |
| `--title` | Nome del prodotto, altrimenti ricavato dalle fonti |
| `--voice` | Narrazione richiesta; disattivata per impostazione predefinita |
| `--no-music`, `--no-sfx` | Disabilitano rispettivamente musica ed effetti |

Una richiesta esplicita in linguaggio naturale equivale all'opzione corrispondente. Non dedurre la lingua dell'output dalla lingua del repository: senza preferenze usa italiano. In caso di opzioni contraddittorie non risolvibili dal contesto, chiedi solo la scelta mancante.

Scrivi piano, brief, testi a schermo e copy in italiano naturale. Conserva nomi propri, marchi e identificatori; non tradurre arbitrariamente etichette presenti nelle schermate reali. Evita calchi, maiuscole all'inglese e slogan generici come “ottimizza il tuo workflow”.

Con `--lang en`, produci testi e materiali in inglese. Con `--lang both`, prepara prima l'italiano e poi una localizzazione inglese dello stesso concept: stessi fatti e branding, testi e tempi adattati separatamente. Non stipare entrambe le lingue nella stessa schermata. Se l'utente chiede invece un unico video con sottotitoli inglesi, segui quella richiesta e verifica i sottotitoli sul montaggio finale.

## 1. Comprendi il prodotto

Leggi README, pagine e componenti principali, flusso utente, CSS/token e asset pertinenti. Parti dalle sorgenti effettive del progetto, senza presumere che esista `index.html`. Con URL o materiali forniti usa gli strumenti disponibili e dichiara i limiti dell'evidenza.

Rispondi nel piano a queste nove domande:
1. Che cosa fa l'app?
2. Qual è il beneficio o elemento sorprendente sostenuto dalle fonti?
3. Qual è l'aggancio visivo più forte?
4. Quale UI, testo o elemento reale mostrerai?
5. Qual è la durata minima efficace?
6. Quale tono e direzione creativa sono adatti?
7. Quale ruolo avrà l'audio?
8. Quale frase accompagnerà la condivisione?
9. Qual è il flusso ingresso → azione → risultato da mostrare?

Se è solo una landing page, dichiaralo e usa il suo elemento più forte. Distingui una ricostruzione animata da una registrazione reale. Non inventare metriche, testimonianze, disponibilità o funzionalità; una parodia non autorizza affermazioni ingannevoli sul prodotto.

## 2. Piano e storyboard

Usa la cartella richiesta dall'utente o dall'ambiente; altrimenti `brag-output/`. Se esiste, crea una variante con timestamp, senza sovrascrivere lavori precedenti. Nella modalità bilingue usa sottocartelle `it/` e `en/`.

Per ogni versione scrivi `brag-plan.md` con risposte, fonti, angolo creativo, palette e font, formato, durata, copy provvisorio e storyboard. Ogni scena indica testo esatto, materiale da mostrare, ingresso/uscita, durata, interazioni simulate, transizione e intenzione audio. Leggi [toni e localizzazione](references/tones.md) quando scegli o affini il tono.

Schema orientativo: apertura 2–3s → presentazione 2–4s → 2–3 momenti chiave → chiusura. Il flusso del prodotto, quando esiste, è il centro del video. Mostra almeno un elemento reale riconoscibile.

Conta la somma delle durate. Mantieni le etichette brevi ferme circa 0,8s e le frasi circa 0,3s per parola, con almeno 1,2s; sono punti di partenza da verificare visivamente. Taglia il testo prima di accelerarlo. Le transizioni e i beat musicali non devono sottrarre tempo alla lettura.

Procedi dopo il piano se la richiesta autorizza il lavoro completo; rispetta eventuali revisioni richieste dall'utente.

## 3. Composizione e audio

Leggi [produzione](references/production.md). Scrivi `composition-brief.md` con percorsi, fonti, storyboard, lingua, identità visiva, audio selezionato e criteri di consegna. Crea il progetto in `composition/` tramite Hyperframes, seguendo la documentazione della versione disponibile. Questa skill possiede concept e contenuti; Hyperframes determina implementazione, animazione e rendering.

## 4. Verifica e consegna

Esegui il controllo della composizione previsto dalla CLI installata, correggi gli errori e genera il render finale. Verifica il file esportato, non soltanto il sorgente: durata e formato, apertura e chiusura, leggibilità, accenti, UI, transizioni, sincronizzazione e audio quando presente. Controlla separatamente IT ed EN.

Estrai `brag.jpg` da un momento forte e stabile, guardalo e correggi la scelta se contiene testo incompleto o transizioni. Non promettere che ogni piattaforma userà il primo frame come thumbnail; consegna il poster separato. Inseriscilo al frame iniziale solo quando utile o richiesto, preservando audio e durata e verificando il nuovo export.

Consegna per ogni lingua `brag.mp4`, `brag.jpg`, `brag-plan.md`, `composition-brief.md`, `share-copy.txt` (1–3 frasi pronte da pubblicare) e `composition/`. Aggiungi il copione solo con voce e i sottotitoli solo se richiesti. Riporta ciò che è stato effettivamente verificato e gli eventuali blocchi. La preparazione del copy non implica pubblicazione sui social.

## English quick start

Use `$italian-saas-brag --lang en` for an English launch teaser, or `--lang both` for separate Italian-first and English versions. Add `--voice` for narration. Preserve verified product claims and adapt each language's timing independently. Default output is Italian, even when the source app is English.

Origine e differenze: [provenienza](references/provenance.md).
