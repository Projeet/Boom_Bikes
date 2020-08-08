mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = 8501\n\
enableCORS=false\n\

" > ~/.streamlit/config.toml
