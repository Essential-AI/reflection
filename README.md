# Rethinking Reflection in Pre-Training

## Abstract
A language model’s ability to reflect on its own reasoning provides a key advantage for solving
complex problems. While most recent research has focused on how this ability develops during
reinforcement learning, we show that it actually begins to emerge much earlier—during the
model’s pre-training. To study this, we introduce deliberate errors into chains-of-thought and
test whether the model can still arrive at the correct answer by recognizing and correcting these
mistakes. By tracking performance across different stages of pre-training, we observe that this
self-correcting ability appears early and improves steadily over time. For instance, an OLMo-2-
7B model pre-trained on 4 trillion tokens displays self-correction on our six self-reflection
tasks.


Stay tuned for code, data and more details!
