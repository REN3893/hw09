def text_editor():
    document = ""
    undo = []
    redo = []

    while True:
        command = input("type/undo/redo/quit: ")

        if(command == "type"):
            text = input("Enter text: ")

            undo.append(document)
            document += text
            redo.clear()
            print("Document:", document)
        elif(command == "undo"):
            if not undo:
                print("Nothing to undo")
            else:
                redo.append(document)
                document = undo.pop()
                print("Document:", document)
        elif(command == "redo"):
            if not redo:
                print("Nothing to redo")
            else:
                undo.append(document)
                document = redo.pop()
                print("Document:", document)
        elif(command == "quit"):
            break
        else:
            print("Invalid command")

text_editor()
