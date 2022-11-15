from setuptools import setup
	
install_requires = [
	"ConfigArgParse",
	"huggingface-hub",
	"numpy ",
	"opencv-python",
	"pandas",
	"Pillow",
	"requests",
	"scikit-learn",
	"scipy",
	"timm @ git+https://github.com/rwightman/pytorch-image-models.git@95feb1da41c1fe95ce9634b83db343e08224a8c5",
	"tokenizers",
	"torch",
	"torchmetrics",
	"torchvision",
	"tqdm",
	"transformer",
	"typing_extensions",
	"urllib3",
	"wandb6",
	"gdown",
	"praw",
	"pmaw",
	"python-dotenv",
	"detoxify"
]

setup(
	name="aestheval",
	install_requires=install_requires,
    packages=['aestheval'],
	version="0.1",
	scripts=[]
)
