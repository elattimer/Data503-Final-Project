-Set up vm with 2+GiB memory

-Reset the logger for appending
https://www.digitalocean.com/community/tutorials/how-to-use-bash-history-commands-and-expansions-on-a-linux-vps

-Install SQL server
curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg

curl -fsSL https://packages.microsoft.com/config/ubuntu/24.04/mssql-server-preview.list | sudo tee /etc/apt/sources.list.d/mssql-server-preview.list

sudo apt-get update
sudo apt-get install -y mssql-server

sudo /opt/mssql/bin/mssql-conf setup
(set the password)

-check the sql server is running
systemctl status mssql-server --no-pager


-Open vm for tunneling
sudo ufw allow 1433/tcp
sudo ufw reload
sudo ss -tlnp | grep 1433

-Start tunnel (exit current terminal)
eval "$(ssh-agent -s)"
ssh-add data-503-project-key.pem

ssh -L 1433:127.0.0.1:1433 azureuser@20.77.48.148

-Define SQL tables
