'''
Pickling is also know as Serialization, Marshalling, Flattening

• Use: To transfer python onjects from one server/ system/ application into
another

It is the process of converting python objects in to byte streams.

Ex_ : The simple example is, two python applications A and B are presented on
two different servers at different locations.

    ― A wants to share python objects to B
        So A will convert his python objects into the byte streams at store it
        in the file (this is know as pickling)
    
    ― B Will take this file and convert it back to the python objects, this
        process is known as unpickling.

Note:
    1. Be cautious about using this at production level applications.
    2. Pickled file has any extension
    3. We have 'pickle' buil-in module

Disadvtanges:
    1. It is advisable not to unpickle data received from an untrusted source
    as they may have security threats.
    2. Pickle module has no way to indetify these threats or malicious data.

How to do this?
-> We have 4 functions present in 'pickle' module
    1) dump() :- py objects --> byte-streams (store into file)
    2) dumps() :- py objects --> byte-streams
    3) load() :- byte-streams --> py objects (read from file)
    4) loads() :- byte-streams --> py objects
'''
# Ex_ Pickling and Unpickling data local, not sharing it with another applic^
import pickle


data = ['pranav', 69, 3.69]

# pickling
byte = pickle.dumps(data)
print('PickledData', byte) # This is pickle byte streamed

# unpickling
pyobj = pickle.loads(byte)
print('\nUnpickled_data', pyobj)    # This is unpickled representation


# ---------------------------------------------------------------------------
# Ex_ Transfer this data to another application; present at another server
new_data = ['pranav', 'Google', 'SDE III']

# File handling operation, wb is -> write mode binary format
f = open("prn.gle", 'wb')
pickle.dump(new_data, f)
f.close()

# A prn.gle file is shared with Applic^2 on different server, unpickled it
f1 = open("prn.gle", 'rb')
received_data = pickle.load(f1)
print(received_data)
