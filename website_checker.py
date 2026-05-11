print("🔍 Website URL checker: ")
url = input("\nEnter the website URL: ")

if url.startswith("https://"):
  print("This website uese HTTPS (secure)")
elif url.startswith("http://"):
  print("This website uese HTTP (not secure)")
else:
  print("Not valid URL")
