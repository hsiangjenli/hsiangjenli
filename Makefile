docker:
	docker run --rm -it -v "/Users/hsiangjenli/Documents/github/hsiangjenli:/manim" manimcommunity/manim

test:
	manim -qm test.py MyGraph