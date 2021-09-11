import React from "react";
import ProductList from "./productList";
import {Route, Switch, useLocation} from 'react-router-dom';
import Product from "./product";
import UserForm from "./userForm";
import PrivateRoute from "./privateRoute";
import Logout from "./logout";
import AddToFavs from "./addToFavs";
import RemoveFromFavs from "./removeFromFavs";

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
                                                 offset={query.get('offset')}/>}/>
            <Route key='category_products'
                   exact
                   path='/category/:slug/products/:pagination?'
                   render={props => <ProductList key={props.location.key}
                                                 limit={query.get('limit')}
                                                 offset={query.get('offset')}/>}/>
            <Route key='products'
                   exact
                   path={['/', '/products/?limit=(\\d+)&offset=(\\d+)', '/products/']}
                   render={props => <ProductList key={props.location.key}
                                                 limit={query.get('limit')}
                                                 offset={query.get('offset')}/>}/>
            <Route key='product_details'
                   exact
                   path='/products/:slug/'
                   render={props => <Product {...props} key={props.location.key}/>}/>
            <Route key='search'
                   exact
                   path='/search/:query?'
                   render={props => <ProductList {...props} key={props.location.key}
                                                 query={query.get('q')}/>}/>
            <Route key='login'
                   exact
                   path={'/login/'}
                   render={() => <UserForm from={window.location.pathname}
                                           action={'login'}/>}/>
            <Route key='register'
                   exact
                   path={'/register/'}
                   render={() => <UserForm from={window.location.pathname}
                                           action={'register'}/>}/>
            <Route path={'/logout/'}
                   exact
                   key='logout'
                   render={() => <Logout/>}/>
            <PrivateRoute path={'/favourites/:pagination?'}
                          exact
                          from={window.location.pathname}
                          limit={query.get('limit')}
                          offset={query.get('offset')}
                          component={ProductList}/>
            <PrivateRoute path={'/add-to-favourites/'}
                          exact
                          component={AddToFavs}/>
            <PrivateRoute path={'/remove-from-favourites/'}
                          exact
                          component={RemoveFromFavs}/>


        </Switch>
    );
}

export default MainContent