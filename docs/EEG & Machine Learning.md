## Introduction
- Machine Learning allows us to use labelled data to train models that can handle temporal patterns automatically and allow us to then predict states (discrete such as sadness, happiness, joy, or dimensional such as the valence/arousal model) for live feeds of EEG data
## Emotions & Labelling
- Emotions can be either Dimensional or Categorical:
	- Dimensional: Emotions placed on two axes, Valence = pleasant/unpleasant, and Arousal = calm/excited.
	- Categorical: happy, sad, angry, indifferent, etc.
### Human EEG
- When labelling EEG data you can use self-report scales where participants rate their emotions after each trial (where something is shown, played for them)
- You can also use standardized stimuli datasets where the content shown to participants is already rated for it's valence, arousal, dominance, category, etc.
- The controlled protocol is a combination of both, which is to play audio, music, induce memories, or show VR/videos, and then use the data's rating & self-report scaled to label the data and establish ground truths
### Emulator / Unlabeled EEG
- Neurosity provides focus/calm metrics for the data being given, and even without those there are many techniques to be applied
### Labeling Strategies for Unlabeled / Emulator Data
- First is to use already present states such as focus/calm and map them to labels
	- for example calm is low arousal, while focus is attention. this can be used for some soft labels later
- Theory based implementations / heuristic labeling, where heuristics are combined into a scoring function and thresholds for classes. Examples:
	- Frontal alpha asymmetry where left > right means positive valence
	- High beta / gamma power and high valence means high arousal
- Labeling From a pretrained model:
	- Train (or use a pre-trained) a model on public data and then use it to label unlabeled data. can be conventional ML with SVMs and RF on band-power features or CNNs/RNNs trained on public data
	- These predictions can then be soft labels for the next step
- Finally, use the heuristics approach with the pretrained-model predictions, emulator labels, etc., to create one consensus label to reduce bias from any of the single functions/columns
- You can also try unsupervised learning to cluster the data and then check and label the clusters manually (*CHECK VALIDITY LATER*)
- LLMs can help generate hypotheses and labeling heuristics (according to recent experiments)

## Limitations of Labeling Data On Emotions & Thoughts
- *Summary*: Technical Limits: few electrodes, low SNR, artifacts, non-stationary signals. Method Limits: small samples, overfitting
- *Subjectivity*: Self reports are inherently personal, and two people may rate the same stimulus (signals) differently, and even one persons rating may vary over time. In practice, the labels (valence/arousal or category) are applied to all EEG data (and it's varience) within a certain time window, which can magnify inaccuracies & promote overfitting
- *Variability*: As mentioned above, the same stimulus rarely shows identical EEG responses in different people. One way to mitigate this is to have training/test sets on separate people to avoid overestimating accuracy
- *Non-Stationary*: EEG signals change due to fatigue, attention, or electrode shifts which messes with the category since all these factors will still produce a signal labeled with 'x' emotion
- *Data Scarcity & Noise*: Most studies have limited trials per person, and even public sets are usually full of subjects, but each subject only gets a few recordings each. You can 'cherry pick' consistent samples which can help highlight common features but ignores nuances and artifacts (eye blinks / muscle noise) that complicate labeling
- *note: All reasons above show's that most models will end up overfitting*
## Conventional ML vs LLM and DL Approaches 
- Conventional ML will end up using handcrafted features (such as ap, probabilities, PSD symmetry, etc.) and train classifiers or regressors to predict labels
	- For these models (SVMs, random forests, etc.) there will need to be cross validation & data augmentation / processing for improved accuracy
		*source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8566577/*
- LLM-driven & Deep Learning are emerging for EEG labeling. For example, a semi-supervised framework combines LLM-based feature extraction with mix-up augmentation (creating synthetic data that's similar to real samples to regularize / reduce overfitting)
	- The “EEG Emotion Copilot” is a lightweight LLM (≈0.5B parameters) fine-tuned for real-time EEG emotion recognition: it classifies incoming EEG via prompt tuning and even generates user feedback and clinical suggestions [here](https://arxiv.org/html/2506.06353v1)
	- Other LLM-inspired models (like EEG2Text or EEG-GPT variants) translate EEG patterns into semantic descriptions or token sequences, effectively aligning brain signals with language representations.
## Leveraging Pre-Trained Models For Performance
- Right now in the project, we are manually extracting features, handling multi-samplingRate streams with different frequencies, and we will eventually be stuck with a small dataset when we start training the models
- But we can leverage Transfer Learning instead, which is when a model is pre-trained on a large general dataset to learn broad features, and then it's applied to a new target task
### Nixon/Keller Crown Dataset
- 133 High-quality EEG sessions from Neurosity crown 3 device
- 8-channel setup covering all brain lobes (C3, C4, CP3, CP4, F5, F6, PO3, PO4)
- Pre-trained ConvTransformer model included
- Check out https://github.com/JeremyNixon/neurosity
- EEG-GPT implementation: https://github.com/neurosity/EEG-GPT
## Emulator -> Real Crown
- there will be a difference in simulated data and real human signals. If we train a model on simulated data it will perform much worse on real data.
- Emulator produces cleaner signals, but has no anatomy variance and models will end up latching to simulator-specific artifacts rather than real markers of emotions/thoughts
- Don't train a model on the emulator data, but only use it to understand the SDK, and build a data pipeline for collection and preprocessing (if need be)
## What All Of The Above Means For The Project
- For our project, we learned how to use the SDK and most of the theory behind the different EEG representations.
- For the dataset we need to perform feature importance analysis to extract the most important features and/or only use raw EEG & calm/focus with a pretrained model
- For labeling data we need to figure out if we want dimensional or categorical labels
- For getting labeled data we can use the focus probability and psd symmetry for heuristic mapping, but for the best results we need a real crown & rated datasets combined with all the input from the sdk
- For the applications of models we can build it will be very limited due to overfitting and other problems mentioned in the previous sections
- To train a model we can either start with Conventional AI, and for new-gen AI we can check Out EEG-GPT, ConvTransformer or EEGPT foundation model for transfer learning on the pre-trained models