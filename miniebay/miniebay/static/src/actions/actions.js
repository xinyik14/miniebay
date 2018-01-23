import AppDispatcher from '../dispatchers/dispatcher';
import Constants from '../constants/constants';

export default {
  loadProducts: (products) => {
    AppDispatcher.handleAction({
      type: Constants.LOAD_PRODUCTS,
      data: products
    })
  },

  filterProducts: (filter) => {
    AppDispatcher.handleAction({
      type: Constants.FILTER_PRODUCTS,
      data: filter
    })
  }
}
