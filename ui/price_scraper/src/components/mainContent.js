import React from "react";
import ProductList from "./productList";
import {Route, Switch} from 'react-router-dom';
import Product from "./product";

class MainContent extends React.Component {
    componentDidMount() {
        console.log("test create")
    }

    render() {
        return (
            <Switch>
                <Route key='products' exact path='/' component={ProductList} />
                <Route key='store_products' exact path='/stores/:slug/products/' component={ProductList} />
                <Route key='category_products' exact path='/category/:slug/products/' component={ProductList} />
                <Route key='product_details' exact path='/products/:slug' component={Product} />
            </Switch>
        );
    }

}

export default MainContent