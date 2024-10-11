preview lecture:
    marp -pw --html --theme custom-theme.css {{lecture}}/slides.md

slides:
    for file in `ls */slides.md`; do \
      marp --theme --html custom-theme.css $file; \
    done
