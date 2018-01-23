import $ from 'jquery';
import Actions from '../actions/actions';

export default {
  getProducts: () => {
    const url = '/api/products'
    $.getJSON(url, (products) => {
      Actions.loadProducts(products)
    })
  }
}
