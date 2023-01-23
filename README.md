# Synchronous_Socket_Encryption (SSE)

* A technique of securing the socket connection between server and the client by using encryption and changing the encryption key in such a way that only server and the client will understand it.
<ul>
The technique works in the following manner:
  <ol>
  <li>First the server generates random set of key values is generated the keys may or may not be unique and can be repeated but not advised.</li>
  <li>Now the server communicates to the client via a public key that is known to both parties.</li>
  <li>Now once the data is gathered from the server the client now uses the public key to decrypt the set of keys.</li>
  <li>Now the client can start communication by choosing the keys from the set.</li>
  <li>After each message sent the client chooses the new key form the set.</li>
  <li>At server side once the client sends the message the sever then decrypts the message by the set of keys it gave to client to encrypt the data.</li>
  <li>In such a way the communication takes place and the connection at each time is secure because of the change in the encryption at each stage which is done synchronously.</li>
  </ol>
</ul>

## Extra: 
<ol>
<li>The pattern of the key synchronization can be changed which will make it much more difficult for hackers to decipher</li>
<li>Also much stronger encryption can be used here we use ceaser cipher to demonstrate this techique</li>
<li>The ammount of set of keys can also change and also be saved for each client so that the secure connection is establised and there will be no need to again send the set of key</li>
<ol>
