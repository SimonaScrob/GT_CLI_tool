# GT_CLI_tool

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
1. If you don't have Python3 installed, doc here: https://phoenixnap.com/kb/how-to-install-python-3-ubuntu 
   
2. Create a virtualenv:
  ```sh
  python3 -m venv app_env
  ```

3. Activate the virtualenv:
  ```sh
  source app_env/bin/activate
 ```

### Installation

1. Generate a service account key:  https://cloud.google.com/iam/docs/creating-managing-service-account-keys
2. Clone the repo
  ```sh
   git clone https://github.com/SimonaScrob/GT_CLI_tool.git
   ```

3. Enter the key you generated in step 1 in `account_key.json` file from `gtd/service_account_keys`
   
4. Run `install.sh` (this will install the required libraries listed in `requirements.txt`, will create the CLI apps `gtranslate`  `gtd`)
 ```sh
      ./install.sh
 ```

<!-- USAGE EXAMPLES -->
### Usage
 ```sh 
 
  (localhost)$ gtd
  Translation daemon started
  (localhost)$ cat > input << EOF
   > Buna dimineata
   > Buona sera
   > Gutten tag
   > Arrivederci
   > EOF   
  (localhost)$ gtranslate -f input -l en
  Translating, please wait…
  Good morning
  Good evening
  Good day
  Goodbye
(localhost)$

```
