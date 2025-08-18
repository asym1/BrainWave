## Electrical Events
- There are 2 different electrical events in neurons
- Action Potentials (spikes): very brief, all or none events used to send signals along axons. Large (at single-cell level) but very shot (1 ms)
- Postsynaptic currents / potentials (PSCs / PSPs): slower voltage changes in neurons following synaptic transmission and last much longer than spikes
## Electroencephalography (EEG)
An EEG records the brain's electrical activity using small electrodes placed on the head to pick up *brain-waves* (summed activity of many neurons). EEG recordings use many scalp electrodes, each measuring the voltage relative to a reference point, so the EEG tracing represents voltage differences over time (instead of just measuring absolute voltage on a graph, its the difference between the voltage & a reference point). In practice, EEG is displayed as multiple channels (pairs of electrodes) plotted versus time

- When many nearby neurons experience PSCs at the same time their electricity adds together and can be measured at the scalp
- EEG mostly measures PSCs, not individual spikes, since PSCs are slower while spikes are brief and contribute very little to low-frequency scalp signals.
- Many "cortical pyramidal" neurons have a similar orientation, allowing their currents to sum coherently and form a net dipole that projects to the scalp. If neurons are randomly oriented or asynchronous, their fields cancel and the scalp electrode (that measures) sees little. These reasons are why cortex (not deep or randomly oriented cells) is the primary visible source for scalp EEG.
- Electrical fields travel through brain tissue, cerebrospinal fluid, skull and scalp before reaching electrodes. Those layers reduce spatial detail (they “blur” the field), which is why EEG localization is approximate and why deep sources are hard to see unless they are strong or propagate to surface cortex.
- Because the signals are so small, The EEG system must filter and amplify them carefully to reduce noise from muscles, eyes, or the environment, and then boosts these microvolt-level signals and converts them to digital form for recording

![diagram of dipoles](/docs/diagram.png)

#### Quote From A [Study](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1012794)
*Here, we performed detailed biophysical and computational modelling of electric field generation in the brain to ascertain the extent to which spiking activity contributes to scalp EEG. We find that it generally does not, suggesting that high frequency broadband EEG signals reflect noise unrelated to brain activity, and validating that low frequency broadband signals are produced by electrical transmission between neurons and not spiking activity. However, our results do characterize a range of frequencies where EEG oscillations may be generated, either in part or in full, by spiking activity. We conclude that spiking activity does not produce broadband signals, but can still generate narrowband signals at high frequencies. Understanding the origins of high-frequency EEG signals has important implications for interpreting scalp recordings and informs the design of quantitative methods for signal analysis.*
## Frequency
- frequency is the number of cycles per second measured in hertz (Hz), so a 10 Hz rhythm completes 10 cycles per second, each one taking 0.1s
- EEG typically considers rhythms across bands (delta, theta, alpha, beta, gamma) with a frequency range, and commonly analyzes power in those bands
	- All brain waves are grouped into these bands with Greek letter names
## Bands
- The main human EEG bands are:
	- **Delta (δ)**: ~0.5–4 Hz (slow waves, seen in deep sleep)
	- **Theta (θ)**: ~4–7 Hz (drowsiness and young children, frontal region) 
	- **Alpha (α)**: ~8–12 Hz seen over the posterior cortex, disappears when eyes open or attention increases (relaxed wakefulness, strongest over parietal/occipital sites)
	- **Mu Rhythm**: ~7-12 Hz seen over the motor cortex ("ears to ears") at rest. Similar to alpha but is centered over the central regions. Attenuates/Desynchronizes during actual or imagined movement
	- **Beta (β)**: ~13–30 Hz (active thinking/intense mental activity, often frontal regions)
- By Measuring the frequency content of the EEG, you can infer brain state
	- e.g. high alpha with closed eyes, delta in deep sleep
- By noting which bands dominate and where they appear on the scalp, clinicians assess brain state and function


## Lobes
- The brain has 4 main lobes: Frontal, Parietal, Occipital, and Temporal
- Certain frequency bands tend to be the strongest over particular lobes as previously mentioned in the Bands section
	- Examples Include: occipital alpha (8–12 Hz) is strongest over the visual cortex, while sensorimotor **mu** (∼8–13 Hz, similar to alpha in frequency but different topography) appears over central/parietal (C3/C4) sites. **frontal-midline theta** (4–8 Hz) is prominent over frontal midline leads during cognitive control
- Although you might now believe that certain frequencies only show up in certain lobes, The previous examples are empirical tendencies, not rules
- In principle, any frequency band can be detected over many lobes, as tendency is not exclusivity, it's just that some bands are stronger in certain areas because of local anatomy and function
## Channels
- And electrode is the physical sensor on the scalp, and the 10-20 system gives standard electrode labels and spacing so recordings are comparable
- A *channel* seen in a recording display is the voltage difference described above. That difference is defined by the montage you choose: Bipolar where each channel is the difference between two neighboring electrodes, or Referential where each channel is the difference between electrode and a common reference. (Referential is usually the one for finding global patterns)
- The number of channels is the number of displayed traces. More channels help separate overlapping sources.
## *Interpreting The EEG*
### Syntax
- With all the previous theory we can now interpret raw EEG time series plots with multiple channels
- Each horizontal trace = one EEG channel (electrode)
- The labels (like CP6, F6, C4, ...) tell you the electrode location following the 10-20 System:
	- F = frontal lobe, C = central (between frontal and parietal), P = parietal, O = occipital
- The x-axis = time
- The y-axis = voltage, usually centered around zero
### Semantics
- Flat lines: no signal or very little change
- Oscillation/Waves: brain activity at that electrode's location
- For each channel, there are different wave speeds (frequencies):
	- Slow big waves: delta/theta (sleepiness, drowsy)
	- Medium faster waves: alpha (relaxed wakefulness)
	- Fast small wiggles: beta/gamma (thinking, movement, attention, depending on which channel)
### Neurosity Channels
- There aren't any *occipital* (vision) or *temporal* (auditory) electrodes in the emulator, it's mostly frontal + motor + parietal.
- *F6, F5* - Frontal Lobe (executive functions, attention, working memory, decision-making)
	- Delta: deep sleep, brain "idling"
	- Theta: working memory, focus under cognitive load
	- Alpha: relaxed wakefulness, inhibition of unnecessary activity
	- Beta: alertness, concentration, decision making
	- Gamma: working memory, conscious attention, problem solving 
- *C3, C4* - Central/motor cortex (movement control: left motor is C3, while right motor is C4)
	- Alpha: (Mu rhythm) motor rest
	- Beta: active movement or motor planning
- *CP3, CP4, CP5, CP6* - Central-parietal junction (sensory-motor integration (linking movement and sensation), body awareness, higher-level processing)
	- Delta: Abnormal if awake, could mean drowsiness or pathology
	- Theta: drowsiness, daydreaming, light sleep
	- Beta: sensory integration
	- Gamma: high-level integration, sensory binding
## Can we use a consumer-grade scalp EEG to classify thoughts?
- consumer headsets (Muse, Neurosity, Emotiv, etc.) can detect **coarse brain states** (drowsiness, rough attention/arousal, movement-related mu suppression in some tasks)
- The literature show promise for limited applications (drowsiness detection, coarse emotion/attention proxies) but also document limitations in signal quality, validation, and reproducibility.
- Technical Limits: few electrodes, low SNR, artifacts, non-stationary signals
- Method Limits: small samples, overfitting
#### Papers on the difficulties and limitations
- https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1289816/full?utm_source
	- "Electroencephalography (EEG) stands as a pioneering tool at the intersection of neuroscience and technology, offering unprecedented insights into human emotions. Through this comprehensive review, we explore the challenges and opportunities associated with EEG-based emotion recognition. While recent literature suggests promising high accuracy rates, these claims necessitate critical scrutiny for their authenticity and applicability. The article highlights the significant challenges in generalizing findings from a multitude of EEG devices and data sources, as well as the difficulties in data collection. Furthermore, the disparity between controlled laboratory settings and genuine emotional experiences presents a paradox within the paradigm of emotion research. We advocate for a balanced approach, emphasizing the importance of critical evaluation, methodological standardization, and acknowledging the dynamism of emotions for a more holistic understanding of the human emotional landscape."
	- "In this comprehensive review, we have shed light on the intricacies of EEG-based emotion recognition. While the allure of high accuracy rates in EEG emotion research paints an optimistic picture, it is essential to approach these claims with cautious optimism. The challenges in generalizing these methods, the inherent discrepancies in laboratory environments, and the dynamic nature of emotions are significant cautions for those eager to adopt EEG in emotion recognition. We must recognize that although EEG holds great potential as a tool in emotion research, its ability to fully understand human emotions is not yet perfect and requires further development and refinement."
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11940461/
	- Abstract: "Background/Objectives: This systematic review presents how neural and emotional networks are integrated into EEG-based emotion recognition, bridging the gap between cognitive neuroscience and practical applications. Methods: Following PRISMA, 64 studies were reviewed that outlined the latest feature extraction and classification developments using deep learning models such as CNNs and RNNs. Results: Indeed, the findings showed that the multimodal approaches were practical, especially the combinations involving EEG with physiological signals, thus improving the accuracy of classification, even surpassing 90% in some studies. Key signal processing techniques used during this process include spectral features, connectivity analysis, and frontal asymmetry detection, which helped enhance the performance of recognition. Despite these advances, challenges remain more significant in real-time EEG processing, where a trade-off between accuracy and computational efficiency limits practical implementation. High computational cost is prohibitive to the use of deep learning models in real-world applications, therefore indicating a need for the development and application of optimization techniques. Aside from this, the significant obstacles are inconsistency in labeling emotions, variation in experimental protocols, and the use of non-standardized datasets regarding the generalizability of EEG-based emotion recognition systems. Discussion: These challenges include developing adaptive, real-time processing algorithms, integrating EEG with other inputs like facial expressions and physiological sensors, and a need for standardized protocols for emotion elicitation and classification. Further, related ethical issues with respect to privacy, data security, and machine learning model biases need to be much more proclaimed to responsibly apply research on emotions to areas such as healthcare, human–computer interaction, and marketing. Conclusions: This review provides critical insight into and suggestions for further development in the field of EEG-based emotion recognition toward more robust, scalable, and ethical applications by consolidating current methodologies and identifying their key limitations."
## References
https://www.sciencedirect.com/science/article/abs/pii/S1556407X12000069 (paid)
https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1012794&utm_source
https://iastate.pressbooks.pub/curehumanphysiology/chapter/eeg/#:~:text=Another%20major%20difference%20between%20the,The%20positively%20charged%20region%20is
