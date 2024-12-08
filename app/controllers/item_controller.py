from flask import Blueprint, jsonify, render_template, request
from app.services.item_service import ItemService

item_controller = Blueprint('item_controller', __name__)

@item_controller.route('/items', methods=['GET'])
def get_all_items():
    items = ItemService.get_all_items()
    return jsonify([item.name for item in items])

@item_controller.route('/item/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = ItemService.get_item_by_id(item_id)
    if item:
        return jsonify({'id': item.id, 'name': item.name, 'description': item.description})
    else:
        return jsonify({'error': 'Item not found'}), 404

@item_controller.route('/item', methods=['POST'])
def create_item():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    
    if name and description:
        new_item = ItemService.create_item(name, description)
        return jsonify({'id': new_item.id, 'name': new_item.name, 'description': new_item.description}), 201
    else:
        return jsonify({'error': 'Invalid data'}), 400
    
@item_controller.route('/items/temp')
def show_items():
    items = ItemService.get_all_items()  # Mendapatkan data item dari service
    return render_template('item_list.html', items=items)
