html:
	python auto_update.py --static $(PWD)/static

gpa:
	python3 core/gpa.py \
		--input config/gpa.xlsx \
		--sheet NTUST-CSIE \
		--bg-logo https://hsiangjenli.github.io/hsiangjenli/static/image/ntust.png\
		--gpa 4.3 \
		--university "National Taiwan University of Science and Technology" \
		--major "Computer Science and Information Engineering" \
		--std_id "M11101T04" \
		--std_name "Hsiang-Jen, Li" \
		--output ntust.html

	python3 core/gpa.py \
		--input config/gpa.xlsx \
		--sheet NKUST-DMB \
		--bg-logo https://hsiangjenli.github.io/hsiangjenli/static/image/nkust.png\
		--gpa 4.3 \
		--university "National Kaohsiung University of Science and Technology" \
		--major "Department of Money and Banking" \
		--std_id "C107125248" \
		--std_name "Hsiang-Jen, Li" \
		--output nkust.html