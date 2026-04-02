from flask import jsonify

def query_all(model, dto_class):
    try:
        records = model.query.all()
        if not records:
            return jsonify([]), 200
        return jsonify([dto_class(r).to_dict() for r in records]), 200
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 500