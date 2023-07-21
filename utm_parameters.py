```python
class UTMParameters:
    def __init__(self, source, medium, campaign, term=None, content=None):
        self.source = source
        self.medium = medium
        self.campaign = campaign
        self.term = term
        self.content = content

    def generate_url(self, base_url):
        utm_url = f"{base_url}?utm_source={self.source}&utm_medium={self.medium}&utm_campaign={self.campaign}"
        if self.term:
            utm_url += f"&utm_term={self.term}"
        if self.content:
            utm_url += f"&utm_content={self.content}"
        return utm_url

def track_cNFT_marketing(base_url, source, medium, campaign, term=None, content=None):
    utm_parameters = UTMParameters(source, medium, campaign, term, content)
    tracking_url = utm_parameters.generate_url(base_url)
    return tracking_url
```