from flask import Flask, request, jsonify,render_template

from Bio import SeqIO
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("blast.html")

@app.route('/blast', methods=['POST'])
def run_blast():
    # Get the uploaded file from the request
    uploaded_file = request.files["file"]
    
    # Do something with the file, e.g. save it to disk or process it
    
    #return "File uploaded successfully"

    # Get the uploaded file from the request
    uploaded_file = request.files['file']
    # Save the file to disk
    file_path = "uploaded.fasta"
    uploaded_file.save(file_path)

    # Call the blast function
    percentage_identity = blast(file_path)
 

    # Return the result as JSON
    return jsonify({'percentage_identity': percentage_identity})

def blast(file1):
# def blast():
#     file1="tp53(3)"
    file2 = "rs1042522.fasta"

    # Read the sequences from the files and split them into words
    with open(file1) as f:
        words1 = set()
        for record in SeqIO.parse(f, "fasta"):
            seq = str(record.seq)
            for i in range(len(seq)-10):
                word = seq[i:i+11]
                words1.add(word)

    with open(file2) as f:
        words2 = set()
        for record in SeqIO.parse(f, "fasta"):
            seq = str(record.seq)
            for i in range(len(seq)-10):
                word = seq[i:i+11]
                words2.add(word)

    # Calculate the percentage identity
    total_words = len(words1.union(words2))
    shared_words = len(words1.intersection(words2))
    percentage_identity = (shared_words / len(words2)) * 100

    # Return the percentage identity
    return percentage_identity

if __name__ == '__main__':
    app.run(debug=True,port="5000")
