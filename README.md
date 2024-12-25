# Mafski

A Flask based math training website built using Openstax math books.

# Setup 
Edit your hosts file (/etc/hosts) adding the hostname mafski to your container ip address.
import the decks you want to work in Anki. Anki has links to each problem. Clicking the link will open the website page with the problem for the student to solve.

# Notes 
You'll need to modify docker-compose.yml to reflect whichever network the container will use.  The anki program is currently hard coded to run the flashcard problems on 172.16.0.17.  I'm certain there's a better way but this was very easy to do.  

```
docker network create \
  --driver bridge \
  --subnet=172.16.0.0/24 \
  caddy
```
Change the ports in docker-compose.yaml and in app.py to reflect which port you want to access.  The Anki deck is set to port 8017.

# Image
The software is functional although it's not really ready for mass distribution via Docker Hub or something like that.  Consider it functional yet still in the beta phase.  I will consider it ready for release when I can make it turnkey.

# Example Usage
Examples to come when I get back to this.
