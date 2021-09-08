import React from "react";
import ProductCard from "./productCard";
import {Link, withRouter} from "react-router-dom";
import {faChevronLeft, faChevronRight} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";

class ProductList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: [],
            previous: null,
            next: null,
            count: null
        };
    }

    componentDidMount() {
        console.log(this.props)
        const location = this.props.location.pathname === '/' ? '/products/' : this.props.location.pathname;
        const limit = this.props.limit ? `?limit=${this.props.limit}` : ''
        const offset = this.props.offset ? `&offset=${this.props.offset}` : ''
        const path = window.location.origin.replace('3000', '8000') + location + limit + offset;
        this.fetchProducts(path);
    }

    fetchProducts(path) {
        fetch(path)
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        items: result.results,
                        previous: result.previous,
                        next: result.next,
                        count: result.count
                    });
                },
                (error) => {
                    this.setState({
                        isLoaded: true,
                        error
                    });
                }
            )
    }

    render() {
        const {error, isLoaded, items} = this.state;
        if (error) {
            return <div>Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Loading...</div>;
        } else {
            console.log(this.state.next, this.state.previous)
            const next = this.state.next && (

                <div className={'next'}>
                    <Link to={this.state.next.replace(/http.?:\/\/[a-z]+:\d*/gm, '')} className={'navigation'}>
                        <FontAwesomeIcon icon={faChevronRight} size={"3x"} color={'#243ce6'}/>
                    </Link>
                </div>
            )
            const previous = this.state.previous && (
                <div className={'previous'}>
                    <Link to={this.state.previous.replace(/http.?:\/\/[a-z]+:\d*/gm, '')} className={'navigation'}>
                        <FontAwesomeIcon icon={faChevronLeft} size={"3x"} color={'#243ce6'}/>
                    </Link>
                </div>

            )
            return (
                <div className={'main-content'}>
                    {previous}
                    <div className={'product-list'}>
                        {items.map((product) => <ProductCard key={product.slug}
                                                             product={product}/>)}
                    </div>
                    {next}
                </div>


            )
        }
    }
}

export default withRouter(ProductList)