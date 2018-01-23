import AppDispatcher from '../dispatchers/dispatcher';
import Constants from '../constants/constants';

export default {
  loadProducts: (products) => {
    AppDispatcher.handleAction({
      type: Constants.LOAD_PRODUCTS,
      data: products
    })
  }
}
