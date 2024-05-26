async function hashAndStore() {
    const input = document.getElementById("userInput").value;
    const timestamp = Math.floor(Date.now() / 1000); // Unix timestamp in seconds

    const hashBuffer = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(input));
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');

    document.getElementById("output").textContent = `Hash: ${hashHex}`;

    // Prepare data for SQLite3
    const data = {
        timestamp: timestamp,
        input: input,
        hash: hashHex
    };

    // SQLite3 interface area
    // this is just a placeholder. In a real app we'd use a library and do some
    // parameterization to prevent sql injection    const safeInput = data.input.replace(/'/g, "''"); 
    const safeInput = data.input.replace(/'/g, "''"); 
    const query = `INSERT INTO hashes (timestamp, input, hash) VALUES (${data.timestamp}, '${safeInput}', '${data.hash}')`;

    executeSQLQuery(query);
}

async function executeSQLQuery(query) {
    const sqlite3 = require('sqlite3').verbose(); 
  
    return new Promise((resolve, reject) => {
      const db = new sqlite3.Database(':memory:', (err) => { 
        if (err) {
          return reject(err); // Reject promise on error
        }
        console.log('Connected to the in-memory SQLite database.');
  
        db.serialize(() => { // Ensure serialized execution
          db.run(`CREATE TABLE IF NOT EXISTS hashes (
            timestamp INTEGER, 
            input TEXT, 
            hash TEXT
          )`, (err) => {
            if (err) {
              return reject(err); // Reject promise on error
            }
            console.log('Table "hashes" created (or already exists).');
  
            // SQL injection prevention (parameterized query)
            const stmt = db.prepare(`INSERT INTO hashes VALUES (?, ?, ?)`);
            stmt.run(data.timestamp, data.input, data.hash, function(err) {
              if (err) {
                return reject(err); // Reject promise on error
              }
              console.log('Inserted row with ID:', this.lastID);
              resolve({ lastID: this.lastID, changes: this.changes }); // Resolve promise with result
            });
            stmt.finalize();
          });
        });
  
        db.close((err) => {
          if (err) {
            return reject(err); // Reject promise on error
          }
          console.log('Closed the database connection.');
        });
      });
    });
  }