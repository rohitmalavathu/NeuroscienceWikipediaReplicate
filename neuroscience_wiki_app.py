import streamlit as st
import re

st.set_page_config(page_title="Neuroscience - Wikipedia", layout="wide")

# --- Wikipedia-like CSS and tooltip styles ---
st.markdown('''
<style>
body, .stApp { background: #fff !important; color: #111 !important; font-family: Georgia, 'Times New Roman', Times, serif; }
#MainHeader { position: sticky; top: 0; background: #fff; z-index: 100; border-bottom: 1px solid #e0e0e0; padding-bottom: 0.5em; }
.wiki-header { font-family: Arial, Helvetica, sans-serif; font-size: 2.2rem; font-weight: 700; color: #111; margin-bottom: 0.1em; }
.wiki-search { width: 100%; max-width: 350px; border-radius: 6px; border: 1px solid #bbb; padding: 0.45em 1em; font-size: 1.1rem; margin-top: 0.2em; }
.wiki-toc { background: #f8f9fa; border: 1px solid #e0e0e0; border-radius: 8px; padding: 1em 1em 1em 1.5em; font-size: 1.05rem; margin-bottom: 1.5em; }
.wiki-toc h2 { font-size: 1.1rem; font-family: Arial, Helvetica, sans-serif; color: #222; margin-bottom: 0.7em; }
.wiki-toc ul { list-style: none; padding-left: 0; }
.wiki-toc li { margin-bottom: 0.3em; }
.wiki-toc a { color: #1565c0; text-decoration: underline; cursor: pointer; }
.wiki-section { font-size: 1.45rem; color: #1a237e; margin-top: 2em; margin-bottom: 0.5em; font-family: Arial, Helvetica, sans-serif; font-weight: 600; }
.wiki-subsection { font-size: 1.15rem; color: #1565c0; margin-top: 1em; margin-bottom: 0.3em; font-family: Arial, Helvetica, sans-serif; font-weight: 500; }
.wiki-link { color: #1565c0; text-decoration: underline; cursor: pointer; }
.tooltip {
  position: relative;
  display: inline-block;
  border-bottom: 1px dotted #1565c0;
  cursor: help;
}
.tooltip .tooltiptext {
  visibility: hidden;
  width: 220px;
  background-color: #f8f9fa;
  color: #222;
  text-align: left;
  border-radius: 6px;
  border: 1px solid #b3c6e0;
  padding: 0.7em 1em;
  position: absolute;
  z-index: 10;
  bottom: 125%;
  left: 50%;
  margin-left: -110px;
  font-size: 0.98rem;
  box-shadow: 0 2px 8px #e0e7ef;
  opacity: 0;
  transition: opacity 0.2s;
}
.tooltip:hover .tooltiptext {
  visibility: visible;
  opacity: 1;
}
@media (max-width: 600px) { .wiki-header { font-size: 1.2rem; } .wiki-section { font-size: 1.1rem; } .wiki-toc { font-size: 0.95rem; } }
</style>
''', unsafe_allow_html=True)

# --- Tooltip definitions for neuroscience terms ---
TOOLTIPS = {
    "prefrontal cortex": "The front part of the frontal lobe, involved in decision-making, planning, and self-control.",
    "amygdala": "An almond-shaped brain region involved in processing emotions, especially fear and pleasure.",
    "hippocampus": "A seahorse-shaped region crucial for forming new memories.",
    "cerebral cortex": "The outer layer of the brain, responsible for higher-order functions like thinking and perception.",
    "neuroplasticity": "The brain's ability to reorganize and form new connections throughout life.",
    "dopamine": "A neurotransmitter involved in reward, motivation, and movement.",
    "synapse": "The junction between two neurons where communication occurs.",
    "neuron": "A nerve cell that transmits information via electrical and chemical signals.",
    "fMRI": "Functional Magnetic Resonance Imaging, a technique for measuring brain activity by detecting changes in blood flow.",
    "EEG": "Electroencephalography, a method to record electrical activity of the brain using electrodes on the scalp.",
    "brain regions": "Distinct anatomical areas of the brain, each with specialized functions (e.g., cortex, hippocampus, amygdala).",
    "neurons": "Nerve cells that are the basic building blocks of the nervous system, transmitting information throughout the body.",
    "synapses": "Connections between neurons where information is transmitted via neurotransmitters.",
    "neurotransmitters": "Chemicals that transmit signals across a synapse from one neuron to another.",
    "electrophysiology": "The study of the electrical properties of biological cells and tissues, especially neurons.",
    "Parkinson's disease": "A neurodegenerative disorder that affects movement, often including tremors.",
    "depression": "A common and serious mood disorder that negatively affects how you feel, think, and act.",
    "brain-computer interfaces": "Systems that enable direct communication between the brain and external devices.",
    "synaptic plasticity": "The ability of synapses to strengthen or weaken over time, essential for learning and memory."
}

def add_tooltips(text):
    # Replace key terms with tooltip HTML
    for term, definition in TOOLTIPS.items():
        pattern = re.compile(rf'\b({re.escape(term)})\b', re.IGNORECASE)
        text = pattern.sub(
            rf'<span class="tooltip">\1<span class="tooltiptext">{definition}</span></span>',
            text)
    return text

# --- Section content (expanded and detailed, no images/visuals) ---
SECTIONS = [
    ("Overview", add_tooltips("""
Neuroscience is the scientific study of the nervous system, including the brain, spinal cord, and networks of [neurons]. It combines biology, psychology, medicine, and computer science to understand how the brain works.

The field explores how [brain regions] interact to produce thoughts, emotions, and behaviors. For example, the [prefrontal cortex] is key for decision-making, while the [amygdala] processes emotional responses.

Neuroscience covers everything from the molecular mechanisms of [synapses] to the complexity of consciousness. It seeks to answer questions like: How do we learn and remember? What causes mental illness? How do drugs affect the brain? The field is highly interdisciplinary, drawing from genetics, pharmacology, engineering, and philosophy.

The nervous system is divided into the central nervous system (CNS), which includes the brain and spinal cord, and the peripheral nervous system (PNS), which connects the CNS to the rest of the body. [neurons] communicate via electrical impulses and chemical signals, forming intricate networks that underlie all behavior and cognition.
""")),
    ("History", add_tooltips("""
The study of the nervous system dates back to ancient Egypt and Greece. In the 19th century, scientists like Santiago Ramón y Cajal used microscopes to reveal the structure of [neurons]. Camillo Golgi developed a staining technique that made it possible to see individual [neurons] for the first time.

The 20th century saw the birth of modern neuroscience, with the discovery of [neurotransmitters], the development of [EEG] and [fMRI], and the rise of computational models of the brain. The Human Connectome Project and BRAIN Initiative are recent large-scale efforts to map brain circuits and understand brain function in health and disease.

Key milestones include the discovery of the action potential, the identification of [dopamine] and serotonin, and the realization that the adult brain is capable of [neuroplasticity].
""")),
    ("Branches of Neuroscience", add_tooltips("""
- **Cognitive neuroscience**: How the brain enables thought, memory, and perception. Example: using [fMRI] to study the [prefrontal cortex] during problem-solving or decision-making tasks.
- **Cellular neuroscience**: How [neurons] and glia function at the cellular level, including ion channels, synaptic transmission, and gene expression.
- **Systems neuroscience**: How networks of [synapses] and [brain regions] process information, such as sensory perception, motor control, and sleep.
- **Computational neuroscience**: Modeling brain function with math and computers, including artificial neural networks and brain simulations.
- **Clinical neuroscience**: Understanding and treating brain disorders, such as [Parkinson's disease], [depression], epilepsy, and schizophrenia. Clinical neuroscience bridges research and medicine, leading to new therapies and diagnostics.
""")),
    ("Research Techniques", add_tooltips("""
- **MRI**: Imaging brain structure in detail, useful for detecting tumors, injuries, and anatomical differences.
- **fMRI**: Imaging brain activity by tracking blood flow changes, often used to study which [brain regions] are active during specific tasks.
- **EEG**: Measuring electrical activity with scalp electrodes, useful for studying sleep, epilepsy, and cognitive processes.
- **Optogenetics**: Using light to control genetically modified [neurons], allowing precise manipulation of brain circuits in animals.
- **Patch clamp**: Measuring currents in single [neurons], revealing how ion channels work.

Other techniques include PET scans, MEG, calcium imaging, and single-cell RNA sequencing. Each method has strengths and limitations in terms of spatial and temporal resolution.
""")),
    ("Major Brain Regions", add_tooltips("""
- <b>Cerebral cortex</b>: Thinking, planning, perception. The cortex is divided into lobes: frontal, parietal, temporal, and occipital, each with specialized functions.
- <b>Prefrontal cortex</b>: Decision-making, self-control, and working memory. Example: The [prefrontal cortex] is highly active when you resist temptation, plan ahead, or solve complex problems.
- <b>Hippocampus</b>: Memory formation and spatial navigation. Example: Taxi drivers have a larger [hippocampus] due to years of navigating city streets.
- <b>Amygdala</b>: Emotional processing, especially fear and pleasure. Example: The [amygdala] is activated during scary movies or when you experience strong emotions.
- <b>Cerebellum</b>: Coordination, balance, and fine motor skills. Damage to the cerebellum can cause ataxia (loss of coordination).
- <b>Brainstem</b>: Basic life functions like breathing, heart rate, and sleep. The brainstem connects the brain to the spinal cord and controls many automatic processes.

Different activities activate different [brain regions]. For example, playing chess engages the [prefrontal cortex] and [hippocampus], while listening to music activates the temporal lobe and [amygdala].
""")),
    ("Applications in Medicine & Tech", add_tooltips("""
Neuroscience research has led to treatments for epilepsy, [depression], and [Parkinson's disease], as well as technologies like [brain-computer interfaces] and neuroprosthetics.

Example: Deep brain stimulation (DBS) can help control tremors in [Parkinson's disease] by targeting specific [brain regions]. Brain-machine interfaces allow paralyzed individuals to control robotic arms with their thoughts. Neuroimaging is used to diagnose brain injuries and guide neurosurgery.

Neuroscience also informs education, mental health, and even marketing (neuromarketing). The field continues to grow as new tools and discoveries emerge.
""")),
    ("Prominent Neuroscientists", add_tooltips("""
- <b>Santiago Ramón y Cajal</b>: Father of modern neuroscience, mapped [neurons] and synapses, and showed that the nervous system is made of discrete cells.
- <b>Rita Levi-Montalcini</b>: Discovered nerve growth factor, crucial for neuron survival and development.
- <b>Eric Kandel</b>: Nobel Prize for research on memory and [synaptic plasticity], showing how learning changes synaptic strength.
- <b>Brenda Milner</b>: Pioneer in memory and cognition, studied the [hippocampus] and patient H.M., revealing how memory is organized in the brain.
- <b>Donald Hebb</b>: Proposed the theory that "neurons that fire together wire together," foundational for understanding learning and [neuroplasticity].
""")),
]

# --- Sticky header with title and search ---
st.markdown("""
<div id='MainHeader'>
  <div style='display:flex; align-items:center; justify-content:space-between;'>
    <div class='wiki-header'>Neuroscience</div>
    <form action="#" method="get" style="margin:0;">
      <input class='wiki-search' name='search' id='searchbox' placeholder='Search Neuroscience...' autocomplete='off' />
    </form>
  </div>
  <div class='wiki-subtitle'>From Wikipedia, the free encyclopedia</div>
</div>
""", unsafe_allow_html=True)

# --- Search logic ---
def search_sections(query):
    q = query.lower()
    found = []
    for i, (heading, content) in enumerate(SECTIONS):
        if q in heading.lower() or q in content.lower():
            found.append((heading, content))
    return found

# --- Left sidebar: Table of Contents ---
st.sidebar.markdown("<div class='wiki-toc'><h2>Contents</h2><ul>" +
    "".join([f"<li><a href='#{heading.lower().replace(' ', '-')}'>{heading}</a></li>" for heading, _ in SECTIONS]) +
    "</ul></div>", unsafe_allow_html=True)

# --- Main content logic ---
search_query = st.experimental_get_query_params().get('search', [''])[0]
if search_query:
    found = search_sections(search_query)
    st.markdown(f"<div class='wiki-header'>Search results for '<b>{search_query}</b>':</div>", unsafe_allow_html=True)
    if found:
        for heading, content in found:
            st.markdown(f"<div class='wiki-section'>{heading}</div>", unsafe_allow_html=True)
            for para in content.split('\n'):
                if para.strip():
                    st.markdown(para, unsafe_allow_html=True)
        st.stop()
    else:
        st.info("No sections found. Try another search.")
        st.stop()

# --- Main article content ---
for i, (heading, content) in enumerate(SECTIONS):
    anchor = heading.lower().replace(' ', '-')
    st.markdown(f"<div class='wiki-section' id='{anchor}'>{heading}</div>", unsafe_allow_html=True)
    # Convert [text] to tooltip if in TOOLTIPS, else plain text
    def tooltipify(text):
        def replace(match):
            term = match.group(1)
            key = term.lower()
            if key in TOOLTIPS:
                definition = TOOLTIPS[key]
                return f"<span class='tooltip'>{term}<span class='tooltiptext'>{definition}</span></span>"
            else:
                return term  # No tooltip, just plain text
        return re.sub(r'\[([^\]]+)\]', replace, text)
    for para in content.split('\n'):
        if para.strip():
            st.markdown(tooltipify(para), unsafe_allow_html=True)

st.markdown("""
---
<div style='text-align:center; font-size:0.95rem;'>This page is for fun and education only. For real brain advice, talk to a neuroscientist or your doctor!</div>
""", unsafe_allow_html=True) 