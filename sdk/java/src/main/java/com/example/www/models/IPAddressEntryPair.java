/*
 * BouncerAPILib
 *
 * This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
 */
package com.example.www.models;

import java.util.*;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonInclude.Include;

@JsonInclude(Include.ALWAYS)
public class IPAddressEntryPair 
        implements java.io.Serializable {
    private static final long serialVersionUID = -7438721582587449028L;
    private String entryID;
    private String iPv4;
    /** GETTER
     * a unique identifier for the newly created Geo Location; opaque but likely a GUID
     */
    @JsonGetter("EntryID")
    public String getEntryID ( ) { 
        return this.entryID;
    }
    
    /** SETTER
     * a unique identifier for the newly created Geo Location; opaque but likely a GUID
     */
    @JsonSetter("EntryID")
    public void setEntryID (String value) { 
        this.entryID = value;
    }
 
    /** GETTER
     * IP Address v4 in CIDR Format. Either IPv4 or IPv6 MUST be present.
     */
    @JsonGetter("IPv4")
    public String getIPv4 ( ) { 
        return this.iPv4;
    }
    
    /** SETTER
     * IP Address v4 in CIDR Format. Either IPv4 or IPv6 MUST be present.
     */
    @JsonSetter("IPv4")
    public void setIPv4 (String value) { 
        this.iPv4 = value;
    }
 
}
