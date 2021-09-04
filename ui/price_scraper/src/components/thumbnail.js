import React from "react";

class Thumbnail extends React.Component {
    render() {
        return (
            <img src={this.props.image_url}  alt={"Product thumbnail"}/>
        )
    }
}

export default Thumbnail