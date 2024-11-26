from flask import Flask, jsonify

from blockchain import Blockchain

app = Flask(__name__)
app.run(host = '0.0.0.0', port = '5000', debug = True)

blockchain = Blockchain()

@app.route('/chain', methods = ['GET'] )
def get_chain():
    return jsonify({
        "total": len(blockchain.chain),
        "rows": blockchain.chain
    }), 200

@app.route('/is_valid', methods = ['GET'])
def validate_chain():

    is_valid = blockchain.is_chain_valid(chain = blockchain.chain)

    return jsonify({
        "valid": is_valid
    }), 200


@app.route('/mine_block', methods = ['GET'] )
def mine_block():
    previous_block = blockchain.get_previous_block()
    
    previous_proof = previous_block['proof']

    proof = blockchain.proof_of_work(previous_proof)

    previous_hash = blockchain.hash(previous_block)

    new_block = blockchain.create_block(proof, previous_hash)

    response = { 
        "message": "Congratulations, you mined one block",
        "index": new_block['index'],
        "timestamp": new_block['timestamp'],
        "proof": new_block['proof'],
        "previous_hash": new_block['previous_hash']
    }

    return jsonify(response), 200






    

