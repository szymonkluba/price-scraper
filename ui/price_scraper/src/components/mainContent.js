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
            <Route key='store_products'
                   exact
                   path='/stores/:slug/products/:pagination?'
                   render={props => <ProductList key={props.location.key}
                                                 limit={query.get('limit')}
                                                 offset={query.get('offset')}/>} />
            <Route key='category_products'
                   exact
                   path='/category/:slug/products/:pagination?'
                   render={props => <ProductList key={props.location.key}
                                                 limit={query.get('limit')}
                                                 offset={query.get('offset')}/>} />
            <Route key='products'
                   exact
                   path={['/', '/products/?limit=(\\d+)&offset=(\\d+)', '/products/']}
                   render={props => <ProductList key={props.location.key}
                                                 limit={query.get('limit')}
                                                 offset={query.get('offset')}/>} />
            <Route key='product_details'
                   exact
                   path='/products/:slug/'
                   render={props => <Product {...props} key={props.location.key}/>} />
            <Route key='search'
                   exact
                   path='/search/:query?'
                   render={props => <ProductList {...props} key={props.location.key}
                                                            query={query.get('q')}/>} />
        </Switch>
    );
}

export default MainContent