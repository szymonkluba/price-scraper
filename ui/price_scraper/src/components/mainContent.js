import React from "react";
import ProductList from "./productList";
import {Route, Switch, useLocation} from 'react-router-dom';
import Product from "./product";

function useQuery() {
    return new URLSearchParams(useLocation().search)
}

function MainContent() {
    let query = useQuery()

    return (
        <Switch>
            <Route key='products'
                   path='/'>
                <ProductList key='products' limit={query.get('limit')} offset={query.get('offset')} />
            </Route>
            <Route key='store_products'
                   path='/stores/:slug/products/'>
                <ProductList key='store_products' limit={query.get('limit')} offset={query.get('offset')} />
            </Route>
            <Route key='category_products'
                   path='/category/:slug/products/'>
                <ProductList key='category_products' limit={query.get('limit')} offset={query.get('offset')} />
            </Route>
            <Route key='product_details'
                   exact
                   path='/products/:slug'>
                <Product key='product_details' />
            </Route>
        </Switch>
    );
}

export default MainContent