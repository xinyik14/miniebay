import $ from 'jquery';
import Actions from '../actions/actions';

export default {
  getProducts: () => {
    const url = '/api/products'
    $.getJSON(url, (products) => {
      Actions.loadProducts(products)
    })
  },

  createProduct: (product, cb) => {
    const url = '/api/products';
    $.ajax ({
      url: url,
      type: "POST",
      data: JSON.stringify(product),
      dataType: "json",
      contentType: "application/json; charset=utf-8",
      success: cb 
    })
  },
}
