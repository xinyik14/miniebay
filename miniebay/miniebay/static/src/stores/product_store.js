import AppDispatcher from '../dispatchers/dispatcher';
import Constants from '../constants/constants';
import {EventEmitter} from 'events';

var products = [];
var productFilter = '';

function loadProducts(data) {
  products = data;
}

class ProductStore extends EventEmitter {
  getState() {
    if (productFilter !== '') {
      return products.filter(product => {
        return product.name.includes(productFilter) || 
          (product.description && product.description.includes(productFilter));
      });
    }
    return products;
  }

  emitChange() {
    this.emit('change');
  }

  addChangeListener(cb) {
    this.on('change', cb);
  }

  removeChangeListener(cb) {
    this.removeListener('change', cb);
  }
}

var _ProductStore = new ProductStore();
export default _ProductStore;

AppDispatcher.register((payload) => {
  var action = payload.action;
  switch(action.type) {
    case Constants.LOAD_PRODUCTS:
      loadProducts(action.data);
      _ProductStore.emitChange();
      break;
    case Constants.FILTER_PRODUCTS:
      productFilter = action.data; 
      _ProductStore.emitChange();
    default:
      break;
  }
});


