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
	"tokenizers",
	"torch",
	"torchmetrics",
	"torchvision",
	"tqdm",
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
