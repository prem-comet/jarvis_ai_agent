from huggingface_hub import login

login("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")

from huggingface_hub import HfApi

api = HfApi()
print(api.whoami())
