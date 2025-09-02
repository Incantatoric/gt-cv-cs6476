<!DOCTYPE html><html>
<head>
    <meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/><title>GT | GT Login</title>

    <link rel="stylesheet" type="text/css" href="/cas/webjars/bootstrap/5.2.0/css/bootstrap.min.css" /><!--[if gte IE 9]><!--><link rel="stylesheet" type="text/css" href="/cas/css/gatech/responsive.css"><!--<![endif]--><!--[if lt IE 9]>
        <script src="/cas/js/html5shiv.min.js"></script>
        <link rel="stylesheet" type="text/css" href="/cas/css/gatech/legacy.css">
    <![endif]--><link rel="icon" href="/cas/favicon.ico" type="image/x-icon"/><script type="text/javascript" src="/cas/webjars/jquery/3.6.1/jquery.min.js"></script>
    <noscript>
        <style type="text/css">
            #cas-content {
                display: none;
            }
        </style>
    </noscript>

</head>

<body id="cas" class="login">
<div id="prefooter">
    <header>
    <div id="identity">
        <h1 id="gt-logo"><a title="Georgia Institute of Technology" rel="home" href="/"><img src="images/gatech/gt-logo-oneline-white.png" alt="Georgia Tech" /></a></h1>
        <h2 id="site-title">Georgia Tech Login Service</h2>
    </div>
    <!-- <section id="primary-menus"> </section> --></header>
<section id="main">
        <div id="content" class="content">
        <noscript>
            <div id="noscript">
                <h2>
                    Click here to sign in
                    
                </h2>
            </div>
        </noscript>
        <div id="cas-content">
            <form method="post" id="fm1" action="login">
    <div class="row">
        <div class="col-md-5 col-12 gx-0 gx-md-4">
            <div  id="login">
                <h2>Enter your GT Account and Password</h2>
                
                <!--[if lte IE 7 ]>
                                <p class="errors">
                                    WARNING: The embedded browser of the windows application you are using is likely to display errors due to its age and incompatibilities. Please click 'Yes' on any boxes that pop up with javascript warnings.
                                </p>
                            <![endif]--><section>
                    <label for="username" ><span class="accesskey">G</span>T Account:</label>
                
                    <div>
                        <input class="required" id="username" size="25" tabindex="1" type="text" accesskey="u" autocomplete="off" name="username" value="" /></div>
                </section>
                
                <section>
                    <label for="password" ><span class="accesskey">P</span>assword:</label>
                
                    <div>
                        <input class="required" type="password" id="password" size="25" tabindex="2"
                            accesskey="p" autocomplete="off" name="password" value="" /><span id="capslock-on" style="display:none;">
                            <p>
                                <i class="fa fa-exclamation-circle"></i>
                                <span >CAPSLOCK key is turned on!</span>
                            </p>
                        </span>
                    </div>
                </section>
                <section class="check">
                    </section>
                
                <section class="btn-row buttons">
                    <input type="hidden" name="execution" value="7c96ce3b-d73c-4585-b4e1-9143d8c037dd_ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0lzSW10cFpDSTZJalkxTVRBell6RmpMVEEyWm1RdE5HTTVOeTFpTldFMkxXVXhOREl5TmpVNVpUWTBaU0o5Lkl1MzBhQ0prVmppazZNVzhlcHl5VUNpX3ZPRDVhdFc5T1pobUxIS0xva2NJRmtCclRmZlBRVm9VUm9INWlqbE5pOEFVNzE4WV90azJ3djlxS2NIcW84ZXd6d2VhVXNVaUdkU2J0dTYwWkNoSHNkSTNXa2NSRnBVeHNCalNoR2ZpZVFpOGloNk1YZGI0XzMyOFB0MlBGMlY0Zkk0TzZSdEVpU0hQbmRNWUwwRVVmb3dSeTNTcm9CQU5FeXpqd19pbjREc2VNYUs1X2U3Sl9iMHdWaEIySjY2UW9VSlpMWWlrOFBPekZJbU1CbjFrbUNkall2dHNwTkFqRzJkZlFicWhMaTkwb2lNaldDQm5wbkkzcmM0WnZhZGFRWE85RXNKVFdvSFcwRTZDaTVWb0RNR19OTnlIdzhYR0p1OFVnVTd3TVU1X3FxX08zLXUxRDdvM2tmWkRibE9rMWdyWlpZRE1rRXRUZWc0ekh4blZjbXQ5LW9sZEY3X1JqQkFvbzl2Y2hfcnVXR2RBM0psVXV6MzNVQkVqV3lpNkRLZGE2b3d1VjdDRmx6cEd6YkdQSFdUTXprYjRpT3FrTXNLNjQtRldfNHVLYzNNclQteTlvbXh4VExfNGQ3MVlhRE85UlNrbUNzclJIOUdIRldaMmMtRzVZTFJIRExuNzYwS3pabXNzaU5wYjBQdUlBN1dnbXB0Yy1zWGhlZ0VoWXlPMEFZYzF6NVowVHIzNFpmZW9DOElzdUNjeVBueElXMnlnWF9MaVdNX2xDSHNFMjQycDdtS0ZWR1lVT3ZPV2U2bE1MMlgxNW1zVlBQZXBWc0QxMDNvVGUtdzlSQnVIQ2c0aGV6VXFidlpGMTVSMkdIM1NSd21vZVE4ZGctYzE4SEw0U3BIbUNabURuSThxQ0Y1cVpHdVV0dHAycXp5R0lMLUFPWExVSDVJTHlJMmlFOExPM3d1WGRrTXRfSktDREtiZ2JtRWlfQ2t6WWZFN2xiNlU2UlZ0OEZ2dlBLVlVfRVJUUDIySk9xaHA2Ynh6dXBqSm54WWJseUc1T3NsZkFWUENTaVAycy1kN3ZHRk5nTElSQXB2STdtbkJJaW1LVWpWSTdHWXR5dU9LWnBfRXRNSGJRSG9CMWxQYy1vSjZCZWsxSTlWZHozSkhBdE9rOEIxT3R6VmI0ZFBqcEE5NEtwX1M5bDVHZV9VSmRzdGp4TTY3c3hZV29GSDlEVklzbE9nUVlZUVl1VnNxNk1GME1Mb19aTFdLN3J2NHM3cHVjNXBUQnlYQzlUMmxMVVN5dEtMWW85WGxTMjd4SmpsdjBNbldoSnY2RHlHZkdaYTFkTTlRTU10UVRnQVI5SUxWRWYzdzlBTmxXSGRRTEhGMEhrdm5nVXpDX3pCNE0wRXVKVzhGd2hDM0trc3c5c2twR3BwMGh3Y1I3OTh0clJDTzV6UWctYUdUUlg0RDNzdG1SejdUd01MQ1BseGJYY3lhOEJPajhtX25UanVaMzEzem0tWGhPZ3l0ZGZGNVRha1Z2RlJOa1hpVGJubDRmUVltS3hNZmJsMndXOVg1Uml4WjlSZ1g5RDRLb3NlLTlpcEwxZmxVMk9QdUZTVmYtaV9lajhFdG5aZXllb3VQY0J2S3dNdG5nWmVDdl9EbVM1aklHdDkxeXZTay0ydU4wUDMtWG1yd051U0pKOWM1TTFQWkI3MXFkZDhaZzFITnIwdE5UTG5JckJkV3BLV3pJTG4zZzdFSEZBdEFfajcycWo4Z0xkcmkwc2wzT3NMRWgwajhtU0JsMmFUUVJOaVZ6LXVoMzl5QldrTEpyWjlsanZFR0thUkpZVGw0em9mNmVwVjF5WUtZTFpZZjZpUDJ3XzZ6Q05pWUxuWXFnM0VfS0FZc0ZFVUV4ZVNTZ0t3TFc3V2paNTdoZ0pGNGExX3FWMGc5Ulk3eTBKV3lhT3BZZEM1RzRwVUhUMWpaSy1GSjAzazdpaHlTRjA2U0NZcEo0eHBRdjN6Vnk3aGVGTVFpLU52REw3aWN5Y3hGMUJYZF85U2tDZlVCWmtkTDlaVXg4LTZEbDFTd2pmWk83Q0NkN2E3UkUwWTU4d0UtQjVSdW5UTWp6Wk5Zb0pJVVY0YzJXTGI5VzRITE4yQUxVUzQ5TlVUYmd6VVFuUXVLbFliZXJSS1FaM2JfWmRoRi1aTVhqMkQ3V1pLdnVtUmljS2Nxb0ZJcVRaVV84QWRwVXVTNlJ2LU95OXp6eDJPblV6Q2NZY1dpQXB3cE1ySmxJLVdaUzl0MnlwQmlwcklnUXVEcWhIMzB0d1VPQW50a2M0V0h2WTREQlp0UFRiOTh3QWRUSFhlbHg3a3dDWDhFcmVHQXc3ek5KemlQbFBwb1J2R0lwR05ucy1iUTNGVVpGX1ZQRGJxM09fMk8xUGhIbzRCUjhHcjFNVFp4YWdpWGdjWkIyVXVORzBDMDc2YWljQUJSRWdrUU1UTDZxWUVydjZTWFlXSEltdlpudzEzSGhmem54UjJfRjFPcC1xUjM3NjdMbllOUzNmcFJObktJT2lUTXprOXJYUEQ4ZVJRaVhOenFFRnQwaHJzbnVONGdsT3ZrNFk2WS1WdVJWR1FmVlVRY3VNUDNXY0lBMVdJdmlCbC1UVG9DbHhPMUxGNXJZVUR2c0NuT3BVRWUzNVZFSlRfeTBJdVZDTEtIcnN6R1MwbVBRX1p3aE42QTJPTHBEZ0d5cnlpeU1nYjExU1Y2SERtdG9CZ1RsaGRHTXZMNDZmVS04V1VpSmVVUTF0eTgxaTVTdkpxVWdXcXU0TnBYR1d6Y2ZOMEluZjhxV3EweUpKREdtWFVUVVN2dHp6ekNROVFxbmFUZjNLX2NscUNhRnN3UFZMb21qdVhkQ2szNGYtT3RZeUwzc3lUNjdTVGYyUkFnWFZIQnd2Wnk4OHVxMUUtS1FiWG1UdjRpMWZTR1NNaTBVdFlZcU1hekhsN3JjM0dKdzZaZ3daX3FvVjhmY2JYTWd2VTA0cHRYOEI0a3JjeXBBM3ZWU0ZsWlVzRFQ0UV9USHdLeXRZVk1FRGlsYTBaanY0YkdiR1FSUFpNTkVPb2l4cG5BdDY2UlJsY3ZKckhEa2RWdEZ2TENvcndUcDRudkh6WjM0d0NyRlN3anE0UnVoX2FOQTYyNFE4d1pxczZkbW1HT2Zqa3Q5V3otMTZOSGhvRU55MHZxMFQ0Mld1cldkZXlPRkxiR1lOUUllMVZwVDNkczZmRlVQTGRNcmtmSS14ZnFwYjNLSmNDaDlhSlpDaENaanphc0JRblROcnFwTThjem1CSXpOdFppVVBrSFB4UDFOX1hYX2JzR2dTUFZFbnRISzdmMk1yeGNMSzBKSlBwWjYxYWZMR2RudGhmd2JSbmR4S1dLcE9BNTZ3VVdXeVhpbmdicGs4cFRSMEpVRFUyZzJ3czNiX3pRY2EwOGxTeXhIbVQ1WVJjcHc0bnRSVEtqdlV0MERhS252WnhXMG5XcmdCTWY5X1gzbF8tUjFudWlGSURtV3JmcW1sc0dYY3RGVTlXeHd5aXg0RkZnLWlnSEtxWXc2RkdGZEVoV2xfdExqYk9XVFBlNUFDNXVpOXdJM0k4RjZiMnZpcnBYWTJNLUhOTFNMV3dSZXE0a1FpZkJJY2Q0THRaR1dfYzF1YzRJeURtYlAxMTg3em9URzBPMmp3bTVJRVE2UWctcTJGeG1tM25OeXlpbVRNNm9SRjZSUXBLS3hDTEF5YnJUaVlsS1lTUk1JQy1oRlBTWmNSWXVPdU5zUVJ4eENfMUVBSy1WMWpZMHpNd3Y3bEVfZjF0LVJLTS1zLXFFSm1rWmQ2V3hGN3FwOWlSeVRteGtBaGVvT0Rob3pvaEllVlVhODY5cEZfNDVaNGRsY2N3cTF0OW5CeWZWVGUwY0RqUG92amZISjdFQUppRlNyU3VzeW1taGJ3d1dEVFpzQmJiOW85d1pfbk0wLWFWSldib0hFNzg2TDhNZmpsVV85c2JoZEdHYUFzMEc0RlZTVll1V0N0a2JLLTZheUJ3S0xCWTFTX0J0V29BTGs4ZDJNalJQZExSdmxwdWRoVGFkeVIyaHliN2cxNW9PSFl4VEFfVDY1X3paejRtbTNSQl9oS1U1UzY3eGpncnRNV3JhSVpiN1laOFF5b0ZUN0E0M1Vic0tlUjhVeGs1eDg1NmZDX0UzZjA0Z3F0a0xpQ1ItQThpV1VWcnNKTTZjQlpVeGF5WGRYY0pYQTM1SVRCMFNjVUFkQnRaOTBPZU9ndXdseWU1Z25pNmkxYVc3ZHE0eklnUmRnaE5BLTJRN0lzekdDelo3YjNXWDBMYXZjTVlUaWxvNURyakFCQXRrVy1TNjNYWDA4M0dRODR0Z0pYd2ViSDlMdGNGakhLX2VKZnJkc05EVC1qZTdibm04N0ZycUNJUHNGWFdWRzBDcE5QY0FUMC13dXFTTnpPVnNaT2RMZE9WdW1sbUNUZzl3SnlzSjRicVF5UDQ5OGtSY2I4dDFrcmJ2V1IxdE5lQmN0cmZsWDNvSWNRY3hqekk3SlpuWGNteXA4VnBndHJSNVFVdGo0Wk1odkxlQjlNMlRHMVBCNHMwX3UzR3Y4N2padl9DVThyX0UtUHFOaUs0SjNPZ1BMbU5HRHlzUmlZUmloRGt1RkgyWGQxZll1RGZMREtrRUd1bGpCeC1aRU9oN0J2d2ZSMXBiNy1uSFUya0lCV1l4QjFIYUIxU2NXN2xXdmxBVjZDRkZEeXNmbjBaNFFLLW5KSzNfaDViU1lNVWFyU2pFUmV6UzhjVjBjU28zNl9iQ05aM1I5Wkl2V1NMaVlBdk9ieEdtMUhoa3M1NkdDWFJ5YmhSeXZHQjRJa21tZjFEV0NiTFJzSVBTM0ZINlZQaEgzRURZc2loaVNHclFkTXFrTGh4OFRRTlBWOW5RMXVKaTZELVFYZnFZRnE4UFd0azg0QnQ3eDRPNTJLVVdEQ2ZzbGEyNmFxRW5lZER1MTNEelo3OUZDdEtCRWNjd0loMFkzdXRqTm9ZT05yT0VUNnlDcGM4S2RCeWZEd1JGdHI3bWNoMVl6WE5zV1RYNkxXQnVnVGd4NkJMbDYtb1VLLTdPeXNTbXVLT3ViNHQ5TGJUM3lreWNSUVhoTWwtMzFERmlUbnZodFhHTWoxR2xRVU5JdmtnamJCUklEOTNOMUpRenRtWWpoWEhPMFZKSmlPNjN5eHEzLVEwcmp6UEJzOWRTbkpWWDVESWIxRTk5SlZiVHl0NUxPQW9WUl9HaUVsYnc1clpTSndOYnBDMUVRc1BhWUdWSTg1TjRhR0ptSlJnTUtIR0JDcHhrWXJuZUY0YXVKZWVsc1VtSTdXamFOYUI5SnFxVjVqWlk5RnVYNkVFS3ozMXZfbWQxNXpTOUxtODVMVW5oVkdtN1VEclpjS1U3bVFVdzc3eXlxdk1iamZBUjNPd01lWEgtWmkybWEyZ2FSM2FLV3hhRTg0WlptZy1TOWM5Rk9SRVN1VUdadGY4LXExZlN3QWg1YVdiZ0Ryc3F1cXlpendObmtUa2Zna0xQOUlIalRGZWlkRUtjWUMwVlpfcC0tVDRmbmRhRDB3VFI5c09abGRvTF9icHVFT0VxSkpXUEY1Z0t2b3VHd0RLcU9XWTctcVI0ckdEOV9Lb24wbVJURGhrbzBLRFU2TWRXcFotdFBfOHlFYkE1T0FnV0QyZjNYeHBkejFHWXQ2WHVPdzg2TnFUNXdyb0V4bTdFMTNjUnpzNHlKd043Zm03el9seXp5NkE5MjFTcTNDVHVwejJFRGNzOXJRdVdYVDdvZDVRcklHTVRLWFVXdEMzYmtYZGtEMElEbGg1VDE3b1FSZmUyTlJCUkg0VzEzYkFTb1Y2RTJ4M01qcjFIeEpsQkdOamI5WnoxNlJYQWxvNWE4N2RnZnUzMUd3ZV9GRzBRWkdmbEQ4dzZKaVBCd05KTmRPTkV2M2p3aFAwWVhYWG1pN0NWWlNGbmEydkVmZVl6V1d2d3NsazlYcWRBT1oxSW16OWVGU3lBdW8wRWFlUnlWS3YwRW1DUkNPMzBoUlVaY0pmUlllcUlodzJpbERkRWU2SEItVWFINjVyVWs2QUR1eDlXRzVsM3lMQlFnMHI3dzctLU1PbkJva25XWUo2RFc0d0ZTNEk5eTVsa0JESkE3azU3d05jVjJMdTFiSElFUjl4YUhCeGNSdi1ETWpmMXQ3aFE2LUhFZGFaSmFnSjdzQXp4R3MzUmxQY0t4aVBSWDRvbTRGcXZSblJ1YUM2YkpXRW1JcUYtWUpkblVrWl85bzhnWWMwUENZZXN1OTR4aWM5WnFLTHVPbi11NXpNdG0teE1MMTk5dy13ZndRdzNfT1dBanMzcmpKbmhLcVhTcHlsVjg1VUc2RHlxZVVGZ0w4YndMb0pEblpKN2JHNEI5MUp3YzVPTnhCeS1YcXVncjhFQ0NFSE12MEFpdjZoVm9NNGlReENGQXhkLTVzbmFUdDJtSTZENHBzYTNXZHkzNUhoUHhvdVYzNm9xcEhRWWhKc0xCZ0FrMWw5YmoyZktucTFwaUhxR1p2MFc2ZTJmZUZDVjU5T2Q2bmxFWkk0RzlGcnFXYlE2RzNfUnBDZ0NQOTZMUS1iZGdIVVkydUZZME12RUNfU2JlVkhHSGtfQlVqNy1SbmpmWEdrZzJaaW5RZFhDcmZ6RUhoVkthWkM5REY4TEhOekQzWWU1c1h0OHdwYkpyVVpJREF6b1hka01pRWF3eVdtRWNBVndVQU9CQUdpbkFTYlBCdDhpaW5uRFZKeVlGaGdrU0g3a1p4VmtXV2JxYWR5VFhuSVJ6bGU5TjRQdEczNWxQV2FwTUtabUlpaWlwSlpCSVc0eHlzcG1vS3Uwd05IbG54N3hHZlpJWDhzZUNmZDlaNUl4OUNhZjZfNVd3US5LOHA4TjQwQjdBUUcxZzh6dlVTV0dUZGVScGFmdnplUkNOVGp0WUc1dlY0TWxnTF9JeGtrNFhvNmtPNmNoTndTS09lRXZUMFEyXzY4cXg4Yy1naXJfQQ==" /><input type="hidden" name="_eventId" value="submit" /><input type="hidden" name="geolocation" /><input class="btn btn-submit button" name="submitbutton" accesskey="l" value="LOGIN"
                        tabindex="6" type="submit" /></section>
                
                <script type="text/javascript">
                    (function () {
                        /*<![CDATA[*/
                        var i = "One moment please...";
                        var j = "LOGIN";
                        /*]]>*/
                        $(window).on('pageshow', function () {
                            $(':submit').prop('disabled', false);
                            $(':submit').prop('value', j);
                        });
                        $(document).ready(function () {
                            $("#fm1").submit(function (event) {
                                $(":submit").prop("disabled", true);
                                $(":submit").prop("value", i);
                                return true;
                            });
                        });
                    })();
                </script>
            </div>
        </div>

        <div class="col-md-7 col-12 gx-0 gx-md-2">
            <div id="loginwarn">
    <p><b>ATTENTION</b>: When you are finished using all of your authenticated applications, please log out of this system and exit your browser to ensure you do not leave any of your applications (such as your e-mail) open to other users of this machine. DUO "GT SSO Beltline" is now "GT SSO-L100".</p>
    <p><b>TERMS OF USE</b><br> This computer system is the property of the Georgia Institute of Technology. Any user of this system must comply with all Institute and Board of Regents policies, including the Acceptable Use Policy, <a href="http://b.gatech.edu/it-policies">Cyber Security Policy and Data Privacy Policy</a>. Users should have no expectation of privacy, as any and all files on this system may be intercepted, monitored, recorded, copied, inspected, and/or disclosed to authorized personnel in order to meet Institute obligations. <br><br> By using this system, I acknowledge and consent to these terms.</p>
    <p>&nbsp;</p>
</div>
<div id="help">
    <div id="dont_know">
       <p><a href="https://passport.gatech.edu/activation/forgot-username">I don't know my GT Account</a></p>
       <p><a href="https://passport.gatech.edu/activation/forgot-password">I don't know my password</a></p>
       <p><a href="https://passport.gatech.edu/two-factor/help">I am unable to use Duo two-factor authentication</a></p>
       <p><a href="https://passport.gatech.edu/?action=check-account-status">My correct username and password aren't working</a></p>
    </div>
    
    <p id="support">
        For assistance, please contact the <a href="https://asc.gatech.edu">Administrative Services Center</a> at <span class="nowrap">404-385-1111.</span>
    </p>
    <p id="additional_info"><a href="http://iamweb1.iam.gatech.edu/docs/Home">Additional documentation including how to integrate your application with GT Login</a></p>
</div>
</div>
    </div>
</form>
<div id="providers" style="display:none">
                <div>
            <script type="text/javascript">
                let providers = [];
            </script>
            <script type="text/javascript">
                /*<![CDATA[*/

                let primaryUrl = null;
                let primaryName = null;

                const redirectTo = $("button[autoRedirectType=client]").attr("id");
                if (primaryUrl != null) {
                    console.log(`Redirecting to primary identity provider ${primaryName} via URL ${primaryUrl}`)
                    let form = document.getElementById(`form${primaryName}`);
                    form.submit();
                }
                else if (redirectTo !== null && redirectTo !== undefined) {
                    console.log(`Redirecting to identity provider URL ${redirectTo}`)
                    let form = document.getElementById(`form${redirectTo}`);
                    form.submit();
                } else {
                    console.log("No identity provider is configured for auto redirection.");
                }
                /*]]>*/
            </script>
        </div>

    </div>
        </div>
    </div>
    </section>
    <section id="superfooter">
    <div id="superfooter-content">&nbsp;</div>
</section>

<footer id="footer">
    <div id="footer-content">
    <ul>
        <li><a href="https://www.gatech.edu/emergency/">Emergency Information</a></li>
        <li><a href="https://www.gatech.edu/legal/">Legal &amp; Privacy Information</a></li>
        <li><a href="https://www.gatech.edu/accessibility/">Accessibility</a></li>
        <li><a href="https://www.gatech.edu/accountability/">Accountability</a></li>
        <li><a href="https://www.gatech.edu/accreditation/">Accreditation</a></li>
        <li><a href="https://www.careers.gatech.edu">Employment</a></li>
    </ul> 

    <!-- TODO: current year --><p>&copy; 2021 Georgia Institute of Technology</p>
</div>
</footer>
</div>
<div><script type="text/javascript" src="/cas/webjars/jquery/3.6.1/jquery.min.js"></script>
<script type="text/javascript" src="/cas/webjars/datatables/1.12.1/js/jquery.dataTables.min.js"></script>

<script type="text/javascript" src="/cas/webjars/es5-shim/4.5.9/es5-shim.min.js"></script>
    <script type="text/javascript" src="/cas/webjars/css-vars-ponyfill/2.4.7/dist/css-vars-ponyfill.min.js"></script>
    <script type="text/javascript" src="/cas/webjars/material-components-web/14.0.0/dist/material-components-web.min.js"></script>
<script type="text/javascript" src="/cas/js/cas.js"></script>
<script type="text/javascript" src="/cas/js/material.js"></script>
<script>
    if (typeof resourceLoadedSuccessfully === "function") {
        resourceLoadedSuccessfully();
    }
    $(() => {
        typeof cssVars === "function" && cssVars({onlyLegacy: true});
    })
    var trackGeoLocation = false;
</script>

</div>

</body>
</html>