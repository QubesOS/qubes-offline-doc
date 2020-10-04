
# This list determines chapters order in the actual output
SOURCES_ALL = build/doc.md \
	$(wildcard doc/introduction/*.md) \
	$(wildcard doc/project-security/*.md) \
	$(wildcard doc/user/hardware/*.md) \
	$(wildcard doc/user/downloading-installing-upgrading/*.md) \
	$(wildcard doc/user/downloading-installing-upgrading/upgrade/*.md) \
	$(wildcard doc/user/common-tasks/*.md) \
	$(wildcard doc/user/managing-os/*.md) \
	$(wildcard doc/user/managing-os/*/*.md) \
	$(wildcard doc/user/advanced-configuration/*.md) \
	$(wildcard doc/user/reference/*.md) \
	$(wildcard doc/developer/general/*.md) \
	$(wildcard doc/developer/code/*.md) \
	$(wildcard doc/developer/system/*.md) \
	$(wildcard doc/developer/services/*.md) \
	$(wildcard doc/developer/debugging/*.md) \
	$(wildcard doc/developer/building/*.md) \
	$(null)

EXCLUDE = \
	doc/introduction/experts.md \
	doc/project-security/canary-checklist.md \
	doc/project-security/canary-template.md \
	doc/project-security/security-bulletins-checklist.md \
	doc/project-security/security-bulletins-template.md \
	doc/project-security/xsa.md \
	doc/developer/general/style-guide.md \
	doc/user/reference/research.md \
	$(null)

SOURCES = $(filter-out $(EXCLUDE), $(SOURCES_ALL))

INTERMEDIATE = $(addprefix build/,$(patsubst %.md,%.json,$(SOURCES)))

all: build/qubes-doc.pdf

# Exclude "Releases" and "External Documentation"
build/doc.md: doc/doc.md
	mkdir -p build
	sed -n -e '/^layout:/a documentclass: scrartcl' \
			-e '0,/### Releases/p' < $< |\
   		head -n -1 > $@

$(INTERMEDIATE): build/%.json: %.md scripts/filter-links.py
	mkdir -p $(dir $@)
	pandoc --filter=scripts/filter-links.py $< -o $@

build/qubes-doc.pdf: $(INTERMEDIATE)
	pandoc --standalone --pdf-engine=xelatex $^ -o $@


install:
	install -m 0644 -D qubes-doc.desktop \
		$(DESTDIR)/usr/share/applications/qubes-doc.desktop
	install -m 0644 -D build/qubes-doc.pdf \
		$(DESTDIR)/usr/share/qubes/qubes-doc.pdf

get-sources:
	git submodule update --init --recursive

verify-sources:
	@true
