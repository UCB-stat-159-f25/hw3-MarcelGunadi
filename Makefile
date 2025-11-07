.PHONY: env html clean

env:
	conda env create -f environment.yml || conda env update -f environment.yml 

html:  
	myst build --html

clean:
	rm -rf figures/* audio/* _build