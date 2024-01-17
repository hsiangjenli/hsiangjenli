html:
	python auto.py

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
		--output static/output/ntust.html

	python3 core/gpa.py \
		--input config/gpa.xlsx \
		--sheet NKUST-DMB \
		--bg-logo https://hsiangjenli.github.io/hsiangjenli/static/image/nkust.png\
		--gpa 4.3 \
		--university "National Kaohsiung University of Science and Technology" \
		--major "Department of Money and Banking" \
		--std_id "C107125248" \
		--std_name "Hsiang-Jen, Li" \
		--output static/output/nkust.html

pdf:
	make gpa
	weasyprint static/output/ntust.html static/pdf/transcript_ntust.pdf
	weasyprint static/output/nkust.html static/pdf/transcript_nkust.pdf


cv:
	python3 auto.py
	weasyprint static/output/cv_eng.html static/pdf/cv_eng.pdf

push:
	git rm -rf hsiangjenli.github.io
	git clone https://github.com/hsiangjenli/hsiangjenli.github.io.git
	git add .
	git commit -m "feat: update template"
	git push origin html5