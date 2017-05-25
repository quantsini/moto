from .responses import StatesResponse

url_bases = [
    "https?://states.(.+).amazonaws.com",
]

url_paths = {
    '{0}/$': StatesResponse.dispatch,
}
