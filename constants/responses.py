from flask import jsonify

def not_found(message):
    return jsonify({
            'error': -1,
            'description': message
        }), 404