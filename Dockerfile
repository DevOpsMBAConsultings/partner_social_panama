FROM odoo:19.0

USER root

# We add --ignore-installed to bypass the Debian/PIP conflict with typing-extensions
RUN pip3 install --no-cache-dir \
    --ignore-installed \
    qifparse \
    "mcp[cli]" \
    httpx \
    --break-system-packages

USER odoo