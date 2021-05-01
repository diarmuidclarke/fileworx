# Admin credentials
- Admin: admin
- pwd: Password0!
<hr>

# Flow of file upload operation

```mermaid
graph TB
  SELFILE['drag or select file']-->CONFDEETS
  CONFDEETS['confirm file metadata and upload path........'] --> STARTUP
  STARTUP['Start upload'] --> FINISHUP
  FINISHUP['Finish upload'] --> EXIT

```