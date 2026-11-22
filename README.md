# Italian SaaS

Una skill per spiegare un prodotto SaaS a chi lo usa. Scegli il materiale da preparare e indica l’applicazione, il progetto o la documentazione di riferimento.

![Illustrazione di un manuale utente e di una registrazione video per un’app SaaS](assets/saas-activity.png)

## Installazione in Codex

Apri un terminale nella cartella `skills/.system/skill-installer` della tua installazione Codex ed esegui il comando seguente.

```sh
python scripts/install-skill-from-github.py --repo VPC3vs/italian-saas-skill-pack --path skills/italian-saas
```

Se il tuo interprete si chiama `python3`, usa quel nome al posto di `python`. In una nuova chat cerca **Italian SaaS** nel selettore delle skill. Usa `$italian-saas` per tutte e tre le modalità.

**Migrazione dalle versioni precedenti.** Se avevi installato `italian-saas-user-manual`, `italian-saas-demo-video` o `italian-saas-brag`, sposta le rispettive cartelle fuori dai percorsi delle skill attive, conservando eventuali modifiche personali. Se esiste già una cartella `italian-saas`, conservane prima una copia fuori dagli stessi percorsi. L’installer richiede una destinazione libera.

## Utilizzo

| Modalità | Esempio | Risultato |
|---|---|---|
| [Manuale utente](skills/italian-saas/modalita/manuale/guida.md) | «Usa $italian-saas per preparare un manuale PDF per gli amministratori di questa app.» | Indice, tono e un esempio di testo da approvare, poi manuale PDF con il marchio del prodotto. |
| [Demo narrata](skills/italian-saas/modalita/demo/guida.md) | «Usa $italian-saas per registrare una demo in italiano del flusso di approvazione.» | Video MP4 del prodotto, voce femminile in italiano, copione completo e sottotitoli quando verificati. |
| [Video di lancio](skills/italian-saas/modalita/lancio/guida.md) | «Usa $italian-saas per creare un teaser verticale di 20 secondi in italiano.» | Teaser, poster e testo per la condivisione, a partire dal brief e dal materiale disponibile. |

Per il lancio sono incluse le guide italiane di **Brag 0.6.0**. Su Codex `/brag` usa il flusso completo e `/brag-slim` seleziona il percorso leggero. Con `--voice` la narrazione usa il flusso completo. L’italiano è la lingua predefinita. Con `--lang en` richiedi l’inglese e con `--lang both` produci due versioni distinte. [Guida Slim](skills/italian-saas/modalita/lancio/slim.md) · [Release Brag 0.6.0](https://github.com/latent-spaces/brag/releases/tag/v0.6.0)

## Strumenti e risorse

- Il manuale richiede materiale sul prodotto e uno strumento per produrre e controllare il PDF.
- Per la demo servono accesso alle schermate, uno strumento di acquisizione e una voce italiana. La guida usa Graphify e Gravity per individuare i flussi del prodotto quando disponibili. Il montaggio locale usa Python e FFmpeg. [Istruzioni per registrazione, voce e montaggio](skills/italian-saas/modalita/demo/references/production.md)
- Per il lancio il pacchetto include le guide tecniche HyperFrames, gli script, la musica e gli effetti. Le guide indicano i programmi necessari alla produzione, tra cui la CLI HyperFrames e gli strumenti audio del percorso scelto. [Guida al montaggio](skills/italian-saas/modalita/lancio/references/step-3-compose.md)

Il progetto e Brag includono le rispettive licenze MIT. Le risorse HyperFrames includono la licenza Apache 2.0. Per musica ed effetti consultare i crediti e le condizioni dei singoli asset. [Licenza del progetto](LICENSE) · [Licenza Brag](skills/italian-saas/modalita/lancio/LICENSE) · [Licenza HyperFrames](skills/italian-saas/modalita/lancio/hyperframes/LICENSE) · [Crediti della musica](skills/italian-saas/modalita/lancio/assets/music/README.md) · [Musica ed effetti](skills/italian-saas/modalita/lancio/references/audio.md)
