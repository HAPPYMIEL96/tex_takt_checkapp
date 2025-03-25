import re
import streamlit as st

st.title("📝 Songtext Takt-Checker")

st.markdown("Gib hier deinen Songtext Zeile für Zeile ein. Das Tool prüft, ob jede Zeile im Takt liegt (ca. 10–12 Silben für 4/4-Takt).")

song_input = st.text_area("🎤 Dein Songtext (jede Zeile einzeln)", height=200)

def count_syllables(line):
    # Sehr einfache Silbenzählung auf Basis von Vokalen
    return len(re.findall(r'[aeiouyäöüAEIOUYÄÖÜ]+', line))

def check_lines_for_rhythm(song_lines):
    feedback = []
    for i, line in enumerate(song_lines, start=1):
        syllables = count_syllables(line)
        if 9 <= syllables <= 13:
            comment = "✅ Gut im Takt (ca. 10–12 Silben)"
        elif syllables < 9:
            comment = "⚠️ Eher zu kurz – evtl. erweitern?"
        else:
            comment = "⚠️ Eher zu lang – evtl. kürzen?"
        feedback.append(f"**Zeile {i}:** {syllables} Silben – {comment}\n> {line}")
    return feedback

if song_input:
    lines = [line.strip() for line in song_input.strip().split("\n") if line.strip()]
    result = check_lines_for_rhythm(lines)

    st.markdown("---")
    st.subheader("🧠 Analyse-Ergebnis")
    for entry in result:
        st.markdown(entry)