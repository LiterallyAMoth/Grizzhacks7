from client import db

def on_snapshot(doc_snapshot, changes, read_time):
    action = changes.document.data["action"]
    if action == "homework time":
        # buzzer on 
        print("homework time!")
    elif action == "arrive":
        # buzzer off 
        print("homeworktime!")
    elif action == "leave":
        # buzzer on
        print("leave")
    elif action == "screenager":
        # squirt
        print("screenager")
doc_ref = db.collection("Oswald").document("Oswald")
doc_watch=doc_ref.on_snapshot(on_snapshot)
