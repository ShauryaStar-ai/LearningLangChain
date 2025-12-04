from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
 @GetMapping("id/{myId}")
    public Object getEntryByID(@PathVariable (name = "myId")String myId) {
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        String userName = authentication.getName();
        User user = userService.findByUserName(userName);
        List<Entry> collection = user.getEntriesByTheUser().stream().filter(x -> x.getId().equals(myId)).collect(Collectors.toList());
        Entry entry;
        if (!collection.isEmpty()) {
            ObjectId id = new ObjectId(myId);
            entry = journaEntryService.findByID(id);
            if (entry != null) {
                // Return 200 OK with the entry
                return ResponseEntity.ok(entry);
            }

        } else {
            // Return 404 Not Found if entry doesn't exist
            return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
        }
        return ResponseEntity.ok(entry);
    }

    @DeleteMapping("{myId}")
    public ResponseEntity<String> removeEntryByID(@PathVariable("myId") String myId ) {

        try {
            Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
            String userName = authentication.getName();
            ObjectId id = new ObjectId(myId);
            journaEntryService.deleteEntryByID(id ,userName);

            // Return a confirmation message with HTTP 200 OK
            return ResponseEntity.ok("Entry with ID " + myId + " deleted successfully!");
        } catch (Exception e) {
            // Return an error message with HTTP 500
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body("Failed to delete entry: " + e.getMessage());
        }
    }
"""
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.JAVA, chunk_size=100, chunk_overlap=20
)
chunks = splitter.split_text(text)
print(len(chunks))
print("This is the second chunk/n"+chunks[0])
print("This is the second chunk/n"+chunks[1])
