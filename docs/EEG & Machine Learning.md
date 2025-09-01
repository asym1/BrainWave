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

## .
## .
## Emulator -> Real Crown
- there will be a difference in simulated data and real human signals. If we train a model on simulated data it will perform much worse on real data.
- Emulator produces cleaner signals, but has no anatomy variance and models will end up latching to simulator-specific artifacts rather than real markers of emotions/thoughts
- Don't train a model on the emulator data, but only use it to understand the SDK, and build a data pipeline for collection and preprocessing (if need be)