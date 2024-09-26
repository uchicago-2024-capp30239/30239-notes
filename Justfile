slides:
    for file in `ls */slides.md`; do \
      marp $file; \
    done
