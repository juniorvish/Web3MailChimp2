# Web3MailChimp2

Web3MailChimp2 is a Web3 alternative to Mailchimp using compressed NFTs (cNFTs). The platform enables mass communication with creators and users through cNFTs, offering a decentralized method of communication and analytics.

## Features

- Integration with Underdog Protocol API to create lists, batch send NFTs, and perform other related functions.
- Integration with Dispatch API for messaging interface to interact with users.
- Utilizing Synap API to get a list of cNFTs.
- CSV upload functionality to import user wallets during drops.
- Interface to view and get notified about cNFTs.
- Embeddable form to collect wallet addresses for sending cNFTs.
- Endpoints for updating metadata on cNFT views.
- Token gating experience for granting access to special features based on the number of cNFTs.
- System to measure open, conversion, and other actions using cNFTs as on-chain stamps or via the site.
- Automating cNFT drops based on a recurring schedule.
- Login system for users to access cNFTs and track their actions.
- Mailchimp Score-like metric to measure user engagement.
- UTM parameters to track the effectiveness of cNFT marketing.
- MVP dashboard for analytics, including on-chain stamps data.

## Getting Started

Clone the repository:

```bash
git clone https://github.com/juniorvish/Web3MailChimp2.git
```

## Usage

Please refer to individual files for usage instructions:

- [Underdog Protocol API Integration](underdog_protocol_api.py)
- [Dispatch API Integration](dispatch_api.py)
- [Synap API Integration](synap_api.py)
- [CSV Upload Functionality](csv_upload.py)
- [cNFT Interface](cnft_interface.py)
- [cNFT Message Drafting](cnft_message_draft.py)
- [cNFT Metadata Endpoint](cnft_metadata_endpoint.py)
- [cNFT Batch Send Endpoint](cnft_batch_send_endpoint.py)
- [Wallet Address Form](wallet_address_form.py)
- [cNFT List Creation](list_creation.py)
- [Token Gating](token_gating.py)
- [cNFT Marketing](cnft_marketing.py)
- [cNFT Dusting](cnft_dusting.py)
- [Action Measurement](action_measurement.py)
- [cNFT Drop Automation](cnft_drop_automation.py)
- [MVP Dashboard](dashboard.py)
- [Login System](login_system.py)
- [Mailchimp Score](mailchimp_score.py)
- [UTM Parameters](utm_parameters.py)

## Resources

- [On-chain Stamps](https://twitter.com/tonyplasencia3/status/1654134691228971009?s=20)
- [Telegram Snapshot](https://twitter.com/BackAnUnderdog/status/1661830970138562560?s=20)

## Note

The information provided here is based on the project description. Actual implementation and development may require additional details and discussions with Tony from Underdog for full integration with their APIs. Make sure that the request response have a body json with same parameter names. There shouldn't be any variable inconsistency.